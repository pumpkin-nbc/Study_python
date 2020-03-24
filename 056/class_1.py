import urllib.request
import os
import random


def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36')
    proxies = ['127.0.0.1:8080']
    proxy = random.choice(proxies)

    proxy_support = urllib.request.proxyHandler({'http':proxy})
    openner = urllib.request.build_opener(proxy_support)
    response = openner.open(url)
    html = response.read()
    return html

def get_page(url):
    html = url_open(url).decode('utf-8')
    a = html.find('')+23
    b = html.find(']',a)
    return html[a:b]

def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []
    a = html.find('')
    while a !=-1:
        b = html.find('.jpg',a,a+255)
        if b !=-1:
            img_addrs.append(html[a+9:b+4])
        else:
            b=a+9
        a = html.find('',b)
    return img_addrs

def save_imgs(folder,img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]
        with open(filename,'wb') as f:
            img = url_open(each)
            f.write(img)

def download_mm(folder='OOXX',pages=10):
    os.mkdir(folder)
    os.chdir(folder)
    url = ''
    page_num=int(get_page(url))
    for i in range(pages):
        page_num -= i
        page_url = url + 'page-' + str(page_num) + '#comments'
        img_addrs = find_imgs(page_url)
        save_imgs(folder,img_addrs)

if __name__ == '__main__':
    download_mm()
