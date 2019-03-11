#!/usr/bin/env python3

import requests
import urllib
from bs4 import BeautifulSoup

quote_page = "https://www.federalreserve.gov/newsevents/pressreleases.htm"
base_url = "https://www.federalreserve.gov"

html = requests.get(
    quote_page).text
bs = BeautifulSoup(html,'lxml')
possible_links = bs.find_all('a')

all_links = [base_url + link.attrs['href'] for link in possible_links]

# Function to delete irrelevant parenthesis in scraped data
def deleteIrrelevant(a):
    front=0
    end=0
    for letter in a:
        if letter=='<':
            front=a.index('<')
            end=front
            while a[end]!='>':
                end+=1
            a = a[:front] + a[end+1:]
        if letter ==',':
            a.replace(',',"")
    return a

#Macro Links to be accessed
parsingLinks = []
for link in all_links:
    if "2017" in link:
        parsingLinks.append(link)
    if "2016" in link:
        parsingLinks.append(link)
    if "2015" in link:
        parsingLinks.append(link)
    if "2014" in link:
        parsingLinks.append(link)
    if "2013" in link:
        parsingLinks.append(link)
    if "2012" in link:
        parsingLinks.append(link)
    if "2011" in link:
        parsingLinks.append(link)


print("Macro-links to be accessed: ")
print(parsingLinks)


#Micro Links in the Macro Links to be accessed
a = []
for link in parsingLinks:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'lxml')
    articleLinks = soup.find_all('a')
    for link in articleLinks:
        a.append(base_url + link.attrs['href'])

##Quarterly Monetary Policies Press Releases
#2017 Monetary Policies Press Releases
mp_201710 = []
mp_201707 = []
mp_201704 = []
mp_201701 = []

#2016 Monetary Policies Press Releases
mp_201610 = []
mp_201607 = []
mp_201604 = []
mp_201601 = []

#2015 Monetary Policies Press Releases
mp_201510 = []
mp_201507 = []
mp_201504 = []
mp_201501 = []

#2014 Monetary Policies Press Releases
mp_201410 = []
mp_201407 = []
mp_201404 = []
mp_201401 = []

#2013 Monetary Policies Press Releases
mp_201310 = []
mp_201307 = []
mp_201304 = []
mp_201301 = []

#2012 Monetary Policies Press Releases
mp_201210 = []
mp_201207 = []
mp_201204 = []
mp_201201 = []

#2011 Monetary Policies Press Releases
mp_201110 = []
mp_201107 = []
mp_201104 = []
mp_201101 = []


#Quarterly organization of Fed Monetary Policy Articles
for each in a:
    #2017 Monetary Policy Articles organized quarterly
    if ("newsevents/pressreleases/monetary" in each and "201711" in each):
        mp_201710.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201710" in each):
        mp_201710.append(each)    
    if ("newsevents/pressreleases/monetary" in each and "201709" in each):
        mp_201707.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201708" in each):
        mp_201707.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201707" in each):
        mp_201707.append(each)    
    if ("newsevents/pressreleases/monetary" in each and "201706" in each):
        mp_201704.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201705" in each):
        mp_201704.append(each)    
    if ("newsevents/pressreleases/monetary" in each and "201704" in each):
        mp_201704.append(each)        
    if ("newsevents/pressreleases/monetary" in each and "201703" in each):
        mp_201701.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201702" in each):
        mp_201701.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201701" in each):
        mp_201701.append(each)
    
    #2016 Monetary Policy Articles quarterly
    if ("newsevents/pressreleases/monetary" in each and "201612" in each):
        mp_201610.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201611" in each):
        mp_201610.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201610" in each):
        mp_201610.append(each)    
    if ("newsevents/pressreleases/monetary" in each and "201609" in each):
        mp_201607.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201608" in each):
        mp_201607.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201607" in each):
        mp_201607.append(each)    
    if ("newsevents/pressreleases/monetary" in each and "201606" in each):
        mp_201604.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201605" in each):
        mp_201604.append(each)    
    if ("newsevents/pressreleases/monetary" in each and "201604" in each):
        mp_201604.append(each)        
    if ("newsevents/pressreleases/monetary" in each and "201603" in each):
        mp_201601.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201602" in each):
        mp_201601.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201601" in each):
        mp_201601.append(each)
    
    #2015 Monetary Policy Articles quarterly
    if ("newsevents/pressreleases/monetary" in each and "201512" in each):
        mp_201510.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201511" in each):
        mp_201510.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201510" in each):
        mp_201510.append(each)    
    if ("newsevents/pressreleases/monetary" in each and "201509" in each):
        mp_201507.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201508" in each):
        mp_201507.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201507" in each):
        mp_201507.append(each)    
    if ("newsevents/pressreleases/monetary" in each and "201506" in each):
        mp_201504.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201505" in each):
        mp_201504.append(each)    
    if ("newsevents/pressreleases/monetary" in each and "201504" in each):
        mp_201504.append(each)        
    if ("newsevents/pressreleases/monetary" in each and "201503" in each):
        mp_201501.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201502" in each):
        mp_201501.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201501" in each):
        mp_201501.append(each)

    #2014 Monetary Policy Articles quarterly
    if ("newsevents/pressreleases/monetary" in each and "201412" in each):
        mp_201410.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201411" in each):
        mp_201410.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201410" in each):
        mp_201410.append(each)    
    if ("newsevents/pressreleases/monetary" in each and "201409" in each):
        mp_201407.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201408" in each):
        mp_201407.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201407" in each):
        mp_201407.append(each)    
    if ("newsevents/pressreleases/monetary" in each and "201406" in each):
        mp_201404.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201405" in each):
        mp_201404.append(each)    
    if ("newsevents/pressreleases/monetary" in each and "201404" in each):
        mp_201404.append(each)        
    if ("newsevents/pressreleases/monetary" in each and "201403" in each):
        mp_201401.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201402" in each):
        mp_201401.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201401" in each):
        mp_201401.append(each)
    
    #2013 Monetary Policy Articles quarterly
    if ("newsevents/pressreleases/monetary" in each and "201312" in each):
        mp_201310.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201311" in each):
        mp_201310.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201310" in each):
        mp_201310.append(each)    
    if ("newsevents/pressreleases/monetary" in each and "201309" in each):
        mp_201307.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201308" in each):
        mp_201307.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201307" in each):
        mp_201307.append(each)    
    if ("newsevents/pressreleases/monetary" in each and "201306" in each):
        mp_201304.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201305" in each):
        mp_201304.append(each)    
    if ("newsevents/pressreleases/monetary" in each and "201304" in each):
        mp_201304.append(each)        
    if ("newsevents/pressreleases/monetary" in each and "201303" in each):
        mp_201301.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201302" in each):
        mp_201301.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201301" in each):
        mp_201301.append(each)
    
    #2012 Monetary Policy Articles quarterly
    if ("newsevents/pressreleases/monetary" in each and "201212" in each):
        mp_201210.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201211" in each):
        mp_201210.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201210" in each):
        mp_201210.append(each)    
    if ("newsevents/pressreleases/monetary" in each and "201209" in each):
        mp_201207.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201208" in each):
        mp_201207.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201207" in each):
        mp_201207.append(each)    
    if ("newsevents/pressreleases/monetary" in each and "201206" in each):
        mp_201204.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201205" in each):
        mp_201204.append(each)    
    if ("newsevents/pressreleases/monetary" in each and "201204" in each):
        mp_201204.append(each)        
    if ("newsevents/pressreleases/monetary" in each and "201203" in each):
        mp_201201.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201202" in each):
        mp_201201.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201201" in each):
        mp_201201.append(each)
    
    #2011 Monetary Policy Articles quarterly
    if ("newsevents/pressreleases/monetary" in each and "201112" in each):
        mp_201110.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201111" in each):
        mp_201110.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201110" in each):
        mp_201110.append(each)    
    if ("newsevents/pressreleases/monetary" in each and "201109" in each):
        mp_201107.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201108" in each):
        mp_201107.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201107" in each):
        mp_201107.append(each)    
    if ("newsevents/pressreleases/monetary" in each and "201106" in each):
        mp_201104.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201105" in each):
        mp_201104.append(each)    
    if ("newsevents/pressreleases/monetary" in each and "201104" in each):
        mp_201104.append(each)        
    if ("newsevents/pressreleases/monetary" in each and "201103" in each):
        mp_201101.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201102" in each):
        mp_201101.append(each)
    if ("newsevents/pressreleases/monetary" in each and "201101" in each):
        mp_201101.append(each)

print()
print("Successfully organized 2011-2017 articles into Quarterly format")


# pmp = Paragraph form of Monetary Policy Articles
# 2017 Monetary Policies
pmp_201710 = ""
pmp_201707 = ""
pmp_201704 = ""
pmp_201701 = ""
# 2016 Monetary Policies
pmp_201610 = ""
pmp_201607 = ""
pmp_201604 = ""
pmp_201601 = ""
# 2015 Monetary Policies
pmp_201510 = ""
pmp_201507 = ""
pmp_201504 = ""
pmp_201501 = ""
# 2014 Monetary Policies
pmp_201410 = ""
pmp_201407 = ""
pmp_201404 = ""
pmp_201401 = ""
# 2013 Monetary Policies
pmp_201310 = ""
pmp_201307 = ""
pmp_201304 = ""
pmp_201301 = ""
# 2012 Monetary Policies
pmp_201210 = ""
pmp_201207 = ""
pmp_201204 = ""
pmp_201201 = ""
# 2011 Monetary Policies
pmp_201110 = ""
pmp_201107 = ""
pmp_201104 = ""
pmp_201101 = ""

###
### Access quarterly data and converts into list of strings for word count
### wmp = Word form of Monetary Policy Articles

###2017 WMPs
for link in mp_201710:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'lxml')
    paragraphFromEachLink = soup.find('div', class_ = 'col-xs-12 col-sm-8 col-md-8').find_all('p')
 
    for word in paragraphFromEachLink:
        pmp_201710 += str(word)

pmp_201710 = deleteIrrelevant(pmp_201710).lower()
wmp_201710 = pmp_201710.split(' ')

for link in mp_201707:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'lxml')
    paragraphFromEachLink = soup.find('div', class_ = 'col-xs-12 col-sm-8 col-md-8').find_all('p')

    for word in paragraphFromEachLink:
        pmp_201707 += str(word)

pmp_201707 = deleteIrrelevant(pmp_201707).lower()
wmp_201707 = pmp_201707.split(' ')

for link in mp_201704:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'lxml')
    paragraphFromEachLink = soup.find('div', class_ = 'col-xs-12 col-sm-8 col-md-8').find_all('p')

    for word in paragraphFromEachLink:
        pmp_201704 += str(word)

pmp_201704 = deleteIrrelevant(pmp_201704).lower()
wmp_201704 = pmp_201704.split(' ')

for link in mp_201701:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'lxml')
    paragraphFromEachLink = soup.find('div', class_ = 'col-xs-12 col-sm-8 col-md-8').find_all('p')

    for word in paragraphFromEachLink:
        pmp_201701 += str(word)

pmp_201701 = deleteIrrelevant(pmp_201701).lower()
wmp_201701 = pmp_201701.split(' ')

###2016 WMPs
for link in mp_201610:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'lxml')
    paragraphFromEachLink = soup.find('div', class_ = 'col-xs-12 col-sm-8 col-md-8').find_all('p')
 
    for word in paragraphFromEachLink:
        pmp_201610 += str(word)

pmp_201610 = deleteIrrelevant(pmp_201610).lower()
wmp_201610 = pmp_201610.split(' ')

for link in mp_201607:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'lxml')
    paragraphFromEachLink = soup.find('div', class_ = 'col-xs-12 col-sm-8 col-md-8').find_all('p')

    for word in paragraphFromEachLink:
        pmp_201607 += str(word)

pmp_201607 = deleteIrrelevant(pmp_201607).lower()
wmp_201607 = pmp_201607.split(' ')

for link in mp_201604:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'lxml')
    paragraphFromEachLink = soup.find('div', class_ = 'col-xs-12 col-sm-8 col-md-8').find_all('p')

    for word in paragraphFromEachLink:
        pmp_201604 += str(word)

pmp_201604 = deleteIrrelevant(pmp_201604).lower()
wmp_201604 = pmp_201604.split(' ')

for link in mp_201601:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'lxml')
    paragraphFromEachLink = soup.find('div', class_ = 'col-xs-12 col-sm-8 col-md-8').find_all('p')

    for word in paragraphFromEachLink:
        pmp_201601 += str(word)

pmp_201601 = deleteIrrelevant(pmp_201601).lower()
wmp_201601 = pmp_201601.split(' ')

###2015 WMPs
for link in mp_201510:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'lxml')
    paragraphFromEachLink = soup.find('div', class_ = 'col-xs-12 col-sm-8 col-md-8').find_all('p')
 
    for word in paragraphFromEachLink:
        pmp_201510 += str(word)

pmp_201510 = deleteIrrelevant(pmp_201510).lower()
wmp_201510 = pmp_201510.split(' ')

for link in mp_201507:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'lxml')
    paragraphFromEachLink = soup.find('div', class_ = 'col-xs-12 col-sm-8 col-md-8').find_all('p')

    for word in paragraphFromEachLink:
        pmp_201507 += str(word)

pmp_201507 = deleteIrrelevant(pmp_201507).lower()
wmp_201507 = pmp_201507.split(' ')

for link in mp_201504:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'lxml')
    paragraphFromEachLink = soup.find('div', class_ = 'col-xs-12 col-sm-8 col-md-8').find_all('p')

    for word in paragraphFromEachLink:
        pmp_201504 += str(word)

pmp_201504 = deleteIrrelevant(pmp_201504).lower()
wmp_201504 = pmp_201504.split(' ')

for link in mp_201501:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'lxml')
    paragraphFromEachLink = soup.find('div', class_ = 'col-xs-12 col-sm-8 col-md-8').find_all('p')

    for word in paragraphFromEachLink:
        pmp_201501 += str(word)

pmp_201501 = deleteIrrelevant(pmp_201501).lower()
wmp_201501 = pmp_201501.split(' ')

###2014 WMPs
for link in mp_201410:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'lxml')
    paragraphFromEachLink = soup.find('div', class_ = 'col-xs-12 col-sm-8 col-md-8').find_all('p')
 
    for word in paragraphFromEachLink:
        pmp_201410 += str(word)

pmp_201410 = deleteIrrelevant(pmp_201410).lower()
wmp_201410 = pmp_201410.split(' ')

for link in mp_201407:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'lxml')
    paragraphFromEachLink = soup.find('div', class_ = 'col-xs-12 col-sm-8 col-md-8').find_all('p')

    for word in paragraphFromEachLink:
        pmp_201407 += str(word)

pmp_201407 = deleteIrrelevant(pmp_201407).lower()
wmp_201407 = pmp_201407.split(' ')

for link in mp_201404:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'lxml')
    paragraphFromEachLink = soup.find('div', class_ = 'col-xs-12 col-sm-8 col-md-8').find_all('p')

    for word in paragraphFromEachLink:
        pmp_201404 += str(word)

pmp_201404 = deleteIrrelevant(pmp_201404).lower()
wmp_201404 = pmp_201404.split(' ')

for link in mp_201401:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'lxml')
    paragraphFromEachLink = soup.find('div', class_ = 'col-xs-12 col-sm-8 col-md-8').find_all('p')

    for word in paragraphFromEachLink:
        pmp_201401 += str(word)

pmp_201401 = deleteIrrelevant(pmp_201401).lower()
wmp_201401 = pmp_201401.split(' ')

###2013 WMPs
for link in mp_201310:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'lxml')
    paragraphFromEachLink = soup.find('div', class_ = 'col-xs-12 col-sm-8 col-md-8').find_all('p')
 
    for word in paragraphFromEachLink:
        pmp_201310 += str(word)

pmp_201310 = deleteIrrelevant(pmp_201310).lower()
wmp_201310 = pmp_201310.split(' ')

for link in mp_201307:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'lxml')
    paragraphFromEachLink = soup.find('div', class_ = 'col-xs-12 col-sm-8 col-md-8').find_all('p')

    for word in paragraphFromEachLink:
        pmp_201307 += str(word)

pmp_201307 = deleteIrrelevant(pmp_201307).lower()
wmp_201307 = pmp_201307.split(' ')

for link in mp_201304:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'lxml')
    paragraphFromEachLink = soup.find('div', class_ = 'col-xs-12 col-sm-8 col-md-8').find_all('p')

    for word in paragraphFromEachLink:
        pmp_201304 += str(word)

pmp_201304 = deleteIrrelevant(pmp_201304).lower()
wmp_201304 = pmp_201304.split(' ')

for link in mp_201301:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'lxml')
    paragraphFromEachLink = soup.find('div', class_ = 'col-xs-12 col-sm-8 col-md-8').find_all('p')

    for word in paragraphFromEachLink:
        pmp_201301 += str(word)

pmp_201301 = deleteIrrelevant(pmp_201301).lower()
wmp_201301 = pmp_201301.split(' ')

###2012 WMPs
for link in mp_201210:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'lxml')
    paragraphFromEachLink = soup.find('div', class_ = 'col-xs-12 col-sm-8 col-md-8').find_all('p')
 
    for word in paragraphFromEachLink:
        pmp_201210 += str(word)

pmp_201210 = deleteIrrelevant(pmp_201210).lower()
wmp_201210 = pmp_201210.split(' ')

for link in mp_201207:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'lxml')
    paragraphFromEachLink = soup.find('div', class_ = 'col-xs-12 col-sm-8 col-md-8').find_all('p')

    for word in paragraphFromEachLink:
        pmp_201207 += str(word)

pmp_201207 = deleteIrrelevant(pmp_201207).lower()
wmp_201207 = pmp_201207.split(' ')

for link in mp_201204:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'lxml')
    paragraphFromEachLink = soup.find('div', class_ = 'col-xs-12 col-sm-8 col-md-8').find_all('p')

    for word in paragraphFromEachLink:
        pmp_201204 += str(word)

pmp_201204 = deleteIrrelevant(pmp_201204).lower()
wmp_201204 = pmp_201204.split(' ')

for link in mp_201201:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'lxml')
    paragraphFromEachLink = soup.find('div', class_ = 'col-xs-12 col-sm-8 col-md-8').find_all('p')

    for word in paragraphFromEachLink:
        pmp_201201 += str(word)

pmp_201201 = deleteIrrelevant(pmp_201201).lower()
wmp_201201 = pmp_201201.split(' ')

###2011 WMPs
for link in mp_201110:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'lxml')
    paragraphFromEachLink = soup.find('div', class_ = 'col-xs-12 col-sm-8 col-md-8').find_all('p')
 
    for word in paragraphFromEachLink:
        pmp_201110 += str(word)

pmp_201110 = deleteIrrelevant(pmp_201110).lower()
wmp_201110 = pmp_201110.split(' ')

for link in mp_201107:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'lxml')
    paragraphFromEachLink = soup.find('div', class_ = 'col-xs-12 col-sm-8 col-md-8').find_all('p')

    for word in paragraphFromEachLink:
        pmp_201107 += str(word)

pmp_201107 = deleteIrrelevant(pmp_201107).lower()
wmp_201107 = pmp_201107.split(' ')

for link in mp_201104:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'lxml')
    paragraphFromEachLink = soup.find('div', class_ = 'col-xs-12 col-sm-8 col-md-8').find_all('p')

    for word in paragraphFromEachLink:
        pmp_201104 += str(word)

pmp_201104 = deleteIrrelevant(pmp_201104).lower()
wmp_201104 = pmp_201104.split(' ')

for link in mp_201101:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'lxml')
    paragraphFromEachLink = soup.find('div', class_ = 'col-xs-12 col-sm-8 col-md-8').find_all('p')

    for word in paragraphFromEachLink:
        pmp_201101 += str(word)

pmp_201101 = deleteIrrelevant(pmp_201101).lower()
wmp_201101 = pmp_201101.split(' ')

print()
print("Successfully converted Quarterly format into Word-Count format")


### Positive and Negative words List

plist = ['strengthen', 'rising', 'rose', 'rise', 'solid', 'boosting', 'stable', 'stability',
          'strong', 'evolve', 'growth', 'grew', 'fostered', 'foster', 'expand', 'expanded',
           'recovery', 'recovering', 'recovered', 'boost', 'certain', 'innovation', 'innovative',
            'development', 'confident', 'expanding', 'stabilize', 'strengthening', 'increase']

nlist = ['disruptions', 'lack', 'disrupted', 'insufficient', 'tight', 'weak', 'depressed', 
         'downward', 'slow', 'deterioration', 'uncertainty', 'deteriorate', 'weaken', 'weakening',
          'stress' , 'stressed', 'drop', 'dropped', 'declined', 'decline', 'fragile', 'below',
          'weaker', 'unstable', 'decreased', 'declines', 'decline', 'decreases', 'soft', 
          'drops', 'slows', 'deteriorates', 'deteriorated', 'weakens', 'slowed' ,'low']


### Positive and Negative word counts initialization
## 2017
pcount201710 = 0
pcount201707 = 0
pcount201704 = 0
pcount201701 = 0

ncount201710 = 0
ncount201707 = 0
ncount201704 = 0
ncount201701 = 0
## 2016
pcount201610 = 0
pcount201607 = 0
pcount201604 = 0
pcount201601 = 0

ncount201610 = 0
ncount201607 = 0
ncount201604 = 0
ncount201601 = 0
## 2015
pcount201510 = 0
pcount201507 = 0
pcount201504 = 0
pcount201501 = 0

ncount201510 = 0
ncount201507 = 0
ncount201504 = 0
ncount201501 = 0
## 2014
pcount201410 = 0
pcount201407 = 0
pcount201404 = 0
pcount201401 = 0

ncount201410 = 0
ncount201407 = 0
ncount201404 = 0
ncount201401 = 0
## 2013
pcount201310 = 0
pcount201307 = 0
pcount201304 = 0
pcount201301 = 0

ncount201310 = 0
ncount201307 = 0
ncount201304 = 0
ncount201301 = 0
## 2012
pcount201210 = 0
pcount201207 = 0
pcount201204 = 0
pcount201201 = 0

ncount201210 = 0
ncount201207 = 0
ncount201204 = 0
ncount201201 = 0
## 2011
pcount201110 = 0
pcount201107 = 0
pcount201104 = 0
pcount201101 = 0

ncount201110 = 0
ncount201107 = 0
ncount201104 = 0
ncount201101 = 0

### Function to count words
def countWords(pnlist, wmp, pncount):
    for x in pnlist:
        for y in wmp:
            if x == y:
                pncount += 1
    return pncount

### 2017
pcount201710 = countWords(plist, wmp_201710, pcount201710)
ncount201710 = countWords(nlist, wmp_201710, ncount201710)
pcount201707 = countWords(plist, wmp_201707, pcount201707)
ncount201707 = countWords(nlist, wmp_201707, ncount201707)
pcount201704 = countWords(plist, wmp_201704, pcount201704)
ncount201704 = countWords(nlist, wmp_201704, ncount201704)
pcount201701 = countWords(plist, wmp_201701, pcount201701)
ncount201701 = countWords(nlist, wmp_201701, ncount201701)

### 2016
pcount201610 = countWords(plist, wmp_201610, pcount201610)
ncount201610 = countWords(nlist, wmp_201610, ncount201610)
pcount201607 = countWords(plist, wmp_201607, pcount201607)
ncount201607 = countWords(nlist, wmp_201607, ncount201607)
pcount201604 = countWords(plist, wmp_201604, pcount201604)
ncount201604 = countWords(nlist, wmp_201604, ncount201604)
pcount201601 = countWords(plist, wmp_201601, pcount201601)
ncount201601 = countWords(nlist, wmp_201601, ncount201601)

### 2015
pcount201510 = countWords(plist, wmp_201510, pcount201510)
ncount201510 = countWords(nlist, wmp_201510, ncount201510)
pcount201507 = countWords(plist, wmp_201507, pcount201507)
ncount201507 = countWords(nlist, wmp_201507, ncount201507)
pcount201504 = countWords(plist, wmp_201504, pcount201504)
ncount201504 = countWords(nlist, wmp_201504, ncount201504)
pcount201501 = countWords(plist, wmp_201501, pcount201501)
ncount201501 = countWords(nlist, wmp_201501, ncount201501)

### 2014
pcount201410 = countWords(plist, wmp_201410, pcount201410)
ncount201410 = countWords(nlist, wmp_201410, ncount201410)
pcount201407 = countWords(plist, wmp_201407, pcount201407)
ncount201407 = countWords(nlist, wmp_201407, ncount201407)
pcount201404 = countWords(plist, wmp_201404, pcount201404)
ncount201404 = countWords(nlist, wmp_201404, ncount201404)
pcount201401 = countWords(plist, wmp_201401, pcount201401)
ncount201401 = countWords(nlist, wmp_201401, ncount201401)

### 2013
pcount201310 = countWords(plist, wmp_201310, pcount201310)
ncount201310 = countWords(nlist, wmp_201310, ncount201310)
pcount201307 = countWords(plist, wmp_201307, pcount201307)
ncount201307 = countWords(nlist, wmp_201307, ncount201307)
pcount201304 = countWords(plist, wmp_201304, pcount201304)
ncount201304 = countWords(nlist, wmp_201304, ncount201304)
pcount201301 = countWords(plist, wmp_201301, pcount201301)
ncount201301 = countWords(nlist, wmp_201301, ncount201301)

### 2012
pcount201210 = countWords(plist, wmp_201210, pcount201210)
ncount201210 = countWords(nlist, wmp_201210, ncount201210)
pcount201207 = countWords(plist, wmp_201207, pcount201207)
ncount201207 = countWords(nlist, wmp_201207, ncount201207)
pcount201204 = countWords(plist, wmp_201204, pcount201204)
ncount201204 = countWords(nlist, wmp_201204, ncount201204)
pcount201201 = countWords(plist, wmp_201201, pcount201201)
ncount201201 = countWords(nlist, wmp_201201, ncount201201)

### 2011
pcount201110 = countWords(plist, wmp_201110, pcount201110)
ncount201110 = countWords(nlist, wmp_201110, ncount201110)
pcount201107 = countWords(plist, wmp_201107, pcount201107)
ncount201107 = countWords(nlist, wmp_201107, ncount201107)
pcount201104 = countWords(plist, wmp_201104, pcount201104)
ncount201104 = countWords(nlist, wmp_201104, ncount201104)
pcount201101 = countWords(plist, wmp_201101, pcount201101)
ncount201101 = countWords(nlist, wmp_201101, ncount201101)

print( "Successfully counted 2011-2017 Quarterly P-N words")

print( "<2017 P-N Count>")
print( "201710, positive: ", pcount201710)
print( "201710, negative: ", ncount201710)
print( "201707, positive: ", pcount201707)
print( "201707, negative: ", ncount201707)
print( "201704, positive: ", pcount201704)
print( "201704, negative: ", ncount201704)
print( "201701, positive: ", pcount201701)
print( "201701, negative: ", ncount201701)
print()
print( "<2016 P-N Count>")
print( "201610, positive: ", pcount201610)
print( "201610, negative: ", ncount201610)
print( "201607, positive: ", pcount201607)
print( "201607, negative: ", ncount201607)
print( "201604, positive: ", pcount201604)
print( "201604, negative: ", ncount201604)
print( "201601, positive: ", pcount201601)
print( "201601, negative: ", ncount201601)
print()
print( "<2015 P-N Count>")
print( "201510, positive: ", pcount201510)
print( "201510, negative: ", ncount201510)
print( "201507, positive: ", pcount201507)
print( "201507, negative: ", ncount201507)
print( "201504, positive: ", pcount201504)
print( "201504, negative: ", ncount201504)
print( "201501, positive: ", pcount201501)
print( "201501, negative: ", ncount201501)
print()
print( "<2014 P-N Count>")
print( "201410, positive: ", pcount201410)
print( "201410, negative: ", ncount201410)
print( "201407, positive: ", pcount201407)
print( "201407, negative: ", ncount201407)
print( "201404, positive: ", pcount201404)
print( "201404, negative: ", ncount201404)
print( "201401, positive: ", pcount201401)
print( "201401, negative: ", ncount201401)
print()
print( "<2013 P-N Count>")
print( "201310, positive: ", pcount201310)
print( "201310, negative: ", ncount201310)
print( "201307, positive: ", pcount201307)
print( "201307, negative: ", ncount201307)
print( "201304, positive: ", pcount201304)
print( "201304, negative: ", ncount201304)
print( "201301, positive: ", pcount201301)
print( "201301, negative: ", ncount201301)
print()
print( "<2012 P-N Count>")
print( "201210, positive: ", pcount201210)
print( "201210, negative: ", ncount201210)
print( "201207, positive: ", pcount201207)
print( "201207, negative: ", ncount201207)
print( "201204, positive: ", pcount201204)
print( "201204, negative: ", ncount201204)
print( "201201, positive: ", pcount201201)
print( "201201, negative: ", ncount201201)
print()
print( "<2011 P-N Count>")
print( "201110, positive: ", pcount201110)
print( "201110, negative: ", ncount201110)
print( "201107, positive: ", pcount201107)
print( "201107, negative: ", ncount201107)
print( "201104, positive: ", pcount201104)
print( "201104, negative: ", ncount201104)
print( "201101, positive: ", pcount201101)
print( "201101, negative: ", ncount201101)
print()