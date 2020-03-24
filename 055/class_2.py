import urllib.request
import random
iplist=['183.195.106.118:8118']
url = 'http://www.whatismyip.com.tw'
proxy_support = urllib.request.ProxyHandler({'http:':random.choices(iplist)})
opener = urllib.request.build_opener(proxy_support)
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36')]
response = opener.open(url)
html = response.read().decode('utf-8')
print(html)