import requests

from bs4 import BeautifulSoup

from recipe_scrapers._utils import on_exception_return

from fake_useragent import UserAgent

import random, json


# some sites close their content for 'bots', so user-agent must be supplied using random user agent
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
            'links',
            'URL',
            'description',
            'imgURL',
            'sodium',
            'fat',
            'cholesterol',
            'carbs',
            'calories',
            'category',
            'datePublished'
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
            response = requests.get(url, headers=self.header, proxies=self.proxy)
            self.soup = BeautifulSoup(response.content, 'lxml')
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

    def URL(self):
        raise NotImplementedError("This should be implemented.")

    def description(self):
        raise NotImplementedError("This should be implemented.")

    def imgURL(self):
        raise NotImplementedError("This should be implemented.")

    def sodium(self):
        raise NotImplementedError("This should be implemented.")

    def fat(self):
        raise NotImplementedError("This should be implemented.")

    def cholesterol(self):
        raise NotImplementedError("This should be implemented.")

    def carbs(self):
        raise NotImplementedError("This should be implemented.")

    def calories(self):
        raise NotImplementedError("This should be implemented.")

    def category(self):
        raise NotImplementedError("This should be implemented.")

    def datePublished(self):
        raise NotImplementedError("This should be implemented.")

    def links(self):
        invalid_href = ('#', '')
        links_html = self.soup.findAll('a', href=True)

        return [
            link.attrs
            for link in links_html
            if link['href'] not in invalid_href
        ]



class JSONScraper():
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
            'links',
            'URL',
            'description',
            'imgURL',
            'sodium',
            'fat',
            'cholesterol',
            'carbs',
            'calories',
            'category'
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
            response = requests.get(url, headers=self.header, proxies=self.proxy)
            self.soup = BeautifulSoup(response.content, 'lxml')

            for recipe in self.soup.find_all('script', type='application/ld+json'):
                self.JSON = recipe.text
            self.data = json.loads(recipe.text)
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

    def URL(self):
        raise NotImplementedError("This should be implemented.")

    def description(self):
        raise NotImplementedError("This should be implemented.")

    def imgURL(self):
        raise NotImplementedError("This should be implemented.")

    def sodium(self):
        raise NotImplementedError("This should be implemented.")

    def fat(self):
        raise NotImplementedError("This should be implemented.")

    def cholesterol(self):
        raise NotImplementedError("This should be implemented.")

    def carbs(self):
        raise NotImplementedError("This should be implemented.")

    def calories(self):
        raise NotImplementedError("This should be implemented.")

    def category(self):
        raise NotImplementedError("This should be implemented.")

    def datePublished(self):
        raise NotImplementedError("This should be implemented.")

    def links(self):
        invalid_href = ('#', '')
        links_html = self.soup.findAll('a', href=True)

        return [
            link.attrs
            for link in links_html
            if link['href'] not in invalid_href
        ]

