class Proxy():

    
    proxies = [] # Will contain proxies [ip, port]

#### adding proxy information so as not to get blocked so fast
    def getProxyList(self):
       # Retrieve latest proxies
       url = 'https://www.sslproxies.org/'
       header = {'User-Agent': str(ua.random)}
       response = requests.get(url, headers=header)
       soup = BeautifulSoup(response.text, 'lxml')
       proxies_table = soup.find(id='proxylisttable')
       try:
           # Save proxies in the array
           for row in proxies_table.tbody.find_all('tr'):
               self.proxies.append({
                   'ip':   row.find_all('td')[0].string,
                   'port': row.find_all('td')[1].string
               })
       except:
           print("error in getting proxy from ssl proxies")
       return proxies
    
    def getProxyList2(self,proxies):
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
                   self.proxies.append({
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
                   self.proxies.append({
                       'ip': row.find_all('td')[1].string,
                       'port': row.find_all('td')[2].string
                   })
       except:
           print("broken")
    
       return proxies
    
    def getProxy(self):
       proxies = self.getProxyList()
       proxies = self.getProxyList2(proxies)
       proxy = random.choice(proxies)
    
       return proxy
#### end proxy info added by ML
