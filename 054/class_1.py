import urllib.request
response = urllib.request.urlopen('http://placekitten.com/600/600')
cat_img = response.read()

with open('cat_600_600.jpg','wb') as f:
    f.write(cat_img)