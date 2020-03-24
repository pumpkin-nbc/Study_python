import urllib.request
import urllib.parse
import json

contect=input('请输入需要翻译的内容:\n')
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
data = {}
data['i'] = contect
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client']='fanyideskweb'
data['salt']='15837654437499'
data['sign']='6dcfa8f73a90383b619d70953717cf05'
data['ts']='1583765443749'
data['bv']='a9c3483a52d7863608142cc3f302a0ba'
data['doctype']='json'
data['version']='2.1'
data['keyfrom']='fanyi.web'
data['action']='FY_BY_CLICKBUTTION'
data=urllib.parse.urlencode(data).encode('utf-8')
response = urllib.request.urlopen(url,data)
html=response.read().decode('utf_8')

target = json.loads(html)
print('翻译结果是:%s' %target['translateResult'][0][0]['tgt'])
