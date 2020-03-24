import urllib.request
response=urllib.request.urlopen("https://ilovefishc.com")
html=response.read()
html=html.decode('utf-8')
print(html)