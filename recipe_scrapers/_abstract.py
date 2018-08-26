from urllib import request

import requests

from bs4 import BeautifulSoup

from recipe_scrapers._utils import on_exception_return

from fake_useragent import UserAgent

import random

from time import sleep


# some sites close their content for 'bots', so user-agent must be supplied
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
}

ua = UserAgent() # From here we generate a random user agent
proxies = [] # Will contain proxies [ip, port]

#### adding proxy information so as not to get blocked so fast
def getProxyList():
    # Retrieve latest proxies
    url = 'https://www.sslproxies.org/'
    header = {'User-Agent': str(ua.random)}
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.text, 'lxml')
    proxies_table = soup.find(id='proxylisttable')
    try:
        # Save proxies in the array
        for row in proxies_table.tbody.find_all('tr'):
            proxies.append({
                'ip':   row.find_all('td')[0].string,
                'port': row.find_all('td')[1].string
            })
    except:
        print("error in getting proxy from ssl proxies")
    return proxies

def getProxyList2(proxies):
    # Retrieve latest proxies
    try:
        url = 'http://list.proxylistplus.com/SSL-List-1'
        header = {'User-Agent': str(ua.random)}
        response = requests.get(url, headers=header)
        soup = BeautifulSoup(response.text, 'lxml')
        proxies_table = soup.find("table", {"class": "bg"})
        #print(proxies_table)
        # Save proxies in the array
        for row in proxies_table.find_all("tr", {"class": "cells"}):
            google = row.find_all('td')[5].string
            if google == "yes":
                #print(row.find_all('td')[1].string)
                proxies.append({
                    'ip': row.find_all('td')[1].string,
                    'port': row.find_all('td')[2].string
                })
    except:
        print("broken")
    # Choose a random proxy
    try:
        url = 'http://list.proxylistplus.com/SSL-List-2'
        header = {'User-Agent': str(ua.random)}
        response = requests.get(url, headers=header)
        soup = BeautifulSoup(response.text, 'lxml')
        proxies_table = soup.find("table", {"class": "bg"})
        # print(proxies_table)
        # Save proxies in the array
        for row in proxies_table.find_all("tr", {"class": "cells"}):
            google = row.find_all('td')[5].string
            if google == "yes":
                #print(row.find_all('td')[1].string)
                proxies.append({
                    'ip': row.find_all('td')[1].string,
                    'port': row.find_all('td')[2].string
                })
    except:
        print("broken")

    return proxies

def getProxy():
    proxies = getProxyList()
    proxies = getProxyList2(proxies)
    proxy = random.choice(proxies)

    return proxy
#### end proxy info added by ML


class AbstractScraper():
    proxy = getProxy()
    header = {'User-Agent': str(ua.random)}

    def __getattribute__(self, name):
        """
        Decorate custom methods to handle exceptions as we want and as we
        specify in the "on_exception_return" method decorator
        """
        to_return = None
        decorated_methods = [
            'title',
            'total_time',
            'instructions',
            'ingredients',
            'links'
        ]
        if name in decorated_methods:
            to_return = ''
        if name == 'total_time':
            to_return = 0
        if name == 'ingredients':
            to_return = []
        if name == 'links':
            to_return = []

        if to_return is not None:
            return on_exception_return(to_return)(object.__getattribute__(self, name))

        return object.__getattribute__(self, name)

    def __init__(self, url, test=False):
        if test:  # when testing, we load a file
            with url:
                self.soup = BeautifulSoup(
                    url.read(),
                    "html.parser"
                )
        else:
            response = requests.get(url, headers=header, proxies=proxy)
            rcode = response.status_code
            print("Status Code - %s " % rcode)

            self.soup = BeautifulSoup(response.content, 'lxml')

            #self.soup = BeautifulSoup(
            #    request.urlopen(request.Request(url, headers=HEADERS)).read(),
            #    "html.parser"
            #)

        self.url = url

    def url(self):
        return self.url

    def host(self):
        """ get the host of the url, so we can use the correct scraper """
        raise NotImplementedError("This should be implemented.")

    def title(self):
        raise NotImplementedError("This should be implemented.")

    def total_time(self):
        """ total time it takes to preparate the recipe in minutes """
        raise NotImplementedError("This should be implemented.")

    def ingredients(self):
        raise NotImplementedError("This should be implemented.")

    def instructions(self):
        raise NotImplementedError("This should be implemented.")

    def links(self):
        invalid_href = ('#', '')
        links_html = self.soup.findAll('a', href=True)

        return [
            link.attrs
            for link in links_html
            if link['href'] not in invalid_href
        ]
