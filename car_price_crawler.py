import sys, os
import urllib2
from BeautifulSoup import *
from urlparse import urljoin
import re

base_url = sys.argv[1]
cost = []
milage = []

#HTTP get request
root_html = urllib2.urlopen(base_url).read()

def scrape_page(url):

    data = urllib2.urlopen(url).read()
    milage_re = re.search(r"(odometer: <b>)(.*?)(<\/b>)", data)
    if milage_re:
        milage.append(int(milage_re.group(2)))

if __name__ == "__main__":

    #get all prices
    for price in BeautifulSoup(root_html, parseOnlyThese=SoupStrainer('span',{'class': 'price'})):
        p = int(price.string[1:])
        if p > 2000:
            cost.append(p)

    #parse and itterate over 'a' tags 
    for link in BeautifulSoup(root_html, parseOnlyThese=SoupStrainer('a',{'class': 'hdrlnk'})):
        scrape_page(urljoin(base_url, link['href']))

    print ""
    print "--------"
    print "avarage cost: $" + str(sum(cost) / len(cost))
    print "avarage milage: " + str(sum(milage) / len(milage))