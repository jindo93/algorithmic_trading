"""
This is a template algorithm on Quantopian for you to adapt and fill in.
"""
from quantopian.algorithm import order_optimal_portfolio
from quantopian.algorithm import attach_pipeline, pipeline_output
from quantopian.pipeline import Pipeline, CustomFactor
from quantopian.pipeline.data.builtin import USEquityPricing
from quantopian.pipeline.factors import AverageDollarVolume
from quantopian.pipeline.filters import Q500US
from quantopian.pipeline.data import Fundamentals
from quantopian.pipeline.factors import SimpleMovingAverage
import quantopian.optimize as opt
import pandas as pd
import numpy as np
import talib


def initialize(context):
    """
    Called once at the start of the algorithm.
    """
    # Rebalance every day, 1 hour after market open.
    schedule_function(my_rebalance, date_rules.every_day(),
                      time_rules.market_open(hours=1))

    # Record tracking variables at the end of each day.
    schedule_function(my_record_vars, date_rules.every_day(),
                      time_rules.market_close())

    schedule_function(frb, date_rules.month_start(), time_rules.market_open())

    # Create our dynamic stock selector.
    attach_pipeline(make_pipeline(), 'my_pipeline')


base_universe = Q500US()

# Custom factor for MACD


class MACD(CustomFactor):
    inputs = [USEquityPricing.close]
    window_length = 60
    mask = base_universe

    # The initial value for EMA is taken as trialing SMA
    def ema(self, data, window):
        c = 2.0 / (window + 1)
        ema = np.mean(data[-(2*window)+1:-window+1], axis=0)
        for value in data[-window+1:]:
            ema = (c * value) + ((1 - c) * ema)
        return ema

    def compute(self, today, assets, out, close):
        fema = self.ema(close, 12)
        sema = self.ema(close, 26)
        macd_line = fema - sema

        # Find trailing macd line
        macd = []
        macd.insert(0, self.ema(close, 12) - self.ema(close, 26))
        for i in range(1, 15, 1):
            macd.insert(0, self.ema(close[:-i], 12) - self.ema(close[:-i], 26))
        signal = self.ema(macd, 9)
        out[:] = macd_line
        #out.signal[:] = signal
        #out.hist[:] = macd_line - signal


class MACD_s(CustomFactor):
    inputs = [USEquityPricing.close]
    window_length = 60
    mask = base_universe

    # The initial value for EMA is taken as trialing SMA
    def ema(self, data, window):
        c = 2.0 / (window + 1)
        ema = np.mean(data[-(2*window)+1:-window+1], axis=0)
        for value in data[-window+1:]:
            ema = (c * value) + ((1 - c) * ema)
        return ema

    def compute(self, today, assets, out, close):
        fema = self.ema(close, 12)
        sema = self.ema(close, 26)
        macd_line = fema - sema

        # Find trailing macd line
        macd = []
        macd.insert(0, self.ema(close, 12) - self.ema(close, 26))
        for i in range(1, 15, 1):
            macd.insert(0, self.ema(close[:-i], 12) - self.ema(close[:-i], 26))
        signal = self.ema(macd, 9)
        out[:] = signal


def make_pipeline():

    print(get_datetime())

    # Base universe set to the Q500US
    base_universe = Q500US()

    lastclose = USEquityPricing.close.latest

    # macd pipeline factor
    myFactor = MACD()
    signal = MACD_s()
    plus = (myFactor > 0)
    mac_s = (myFactor > signal)

    # sma difference
    mean_close_25 = SimpleMovingAverage(
        inputs=[USEquityPricing.close],
        window_length=30,
        mask=base_universe
    )

    limit_bound = mean_close_25 * 0.95
    upper_bound = mean_close_25 * 1.04
    lower_bound = mean_close_25 * 0.99

    checks_l = lastclose < lower_bound

    # holder
    longs = plus & mac_s & checks_l

    # securities to trade
    securities_to_trade = (longs)

    return Pipeline(
        columns={
            'longs': longs}, screen=(securities_to_trade)
    )

    # target weight calcuation


def compute_target_weights(context, data):

    weights = {}

    # if there are securities in our long lists and short lists
    # compute even target weights for each security

    if context.longs:
        long_weight = 1.0 / len(context.longs)
    else:
        return weights

    # Exit positions in our portfolio if they are not
    # in our longs or shorts lists.

    for security in context.portfolio.positions:
        prices = data.history(security, 'price', 25, '1d')
        macd_raw, signal, hist = talib.MACD(prices, fastperiod=12,
                                            slowperiod=26, signalperiod=9)
        macd = macd_raw[-1] - signal[-1]
        current_position = context.portfolio.positions[security].amount
        if macd < 0 and current_position > 0 and data.can_trade(security):
            weights[security] = 0

    for security in context.longs:
        weights[security] = long_weight

    return weights


fd = []


def frb(context, data):
    fd.append(1)


def before_trading_start(context, data):
    f = [0.552, 0.714, 0.714, 0.714, 0.8, 0.8, 0.8, 0.667,
         0.667, 0.667, 0.69, 0.69, 0.69, 0.650, 0.650]
    if f[len(fd)] > 0.6:
        bound = [1.04, 0.99]
    elif f[len(fd)] > 0.55:
        bound = [1.03, 0.98]
    elif f[len(fd)] > 0.50:
        bound = [1.025, 1.025]
    elif f[len(fd)] > 0.45:
        bound = [1.02, 0.97]
    else:
        bound = [1.01, 0.96]

    """
    Called every day before market open.
    """
    pipe_results = pipeline_output('my_pipeline')

    # Go long in securities for which the 'longs' value is True,
    # and check if they can be traded.
    context.longs = []
    for sec in pipe_results[pipe_results['longs']].index.tolist():
        prices = data.history(sec, 'close', 30, '1d').mean()
        price_m = data.history(sec, 'close', 1, '1d')
        if data.can_trade(sec) and (price_m < prices * bound[1])[0]:
            context.longs.append(sec)


def my_rebalance(context, data):
    # Calculate target weights to rebalance
    target_weights = compute_target_weights(context, data)

    # If we have target weights, rebalance our portfolio
    if target_weights:
        order_optimal_portfolio(
            objective=opt.TargetWeights(target_weights),
            constraints=[],
        )


def my_record_vars(context, data):
    longs = shorts = 0
    for position in context.portfolio.positions.itervalues():
        if position.amount > 0:
            longs += 1
        elif position.amount < 0:
            shorts += 1

    # Record our variables.
    record(
        leverage=context.account.leverage,
        long_count=longs
    )


def handle_data(context, data):
    """
    Called every minute.
    """
    pass
