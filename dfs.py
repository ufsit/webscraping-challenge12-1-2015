import sys, os
import urllib2
from BeautifulSoup import *
from urlparse import *

def dfs(url, callback, urls = [], depth = 1, max_depth = 10):
    """
    recursive depth-first search for links
    """

    #base case
    if (depth > max_depth) or (url in urls):
        return
    else:

        #make sure we do not revisit
        urls.append(url)

        #HTTP get request
        root_html = urllib2.urlopen(url).read()

        callback(url, root_html)

        #parse and itterate over 'a' tags 
        for link in BeautifulSoup(root_html, parseOnlyThese=SoupStrainer('a')):

            try:
            	#ignore the inner links
                if not (link['href'].startswith('#') or link['href'].startswith('?')):

                    #find the absolute path
                    next = urljoin(url, link['href'])
                    dfs(next, callback, urls, depth + 1, max_depth)

            except Exception as e:
                print e

if __name__ == "__main__": 
    """crawls an apachee dir and prints out all of the paths discovered"""

    base_url = sys.argv[1]

    def cb(url, html):
        print url.replace(base_url, '')

    dfs(base_url, cb)