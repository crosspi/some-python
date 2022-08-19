import requests

url = "https://api.ahfi.cn/api/lsjt?format=json"

payload={}
headers = {
  'Cache-Control': 'no-cache',
  'Accept': '*/*',
  'Accept-Encoding': 'gzip, deflate',
  'Connection': 'keep-alive'
}

response = requests.request("GET", url, headers=headers, data=payload)

history=response.text
history=eval(history)
print('今天是:%s'%history.get('day'))
print('历史上的今天发生了:')
list1=history.get('content')
ii=1
for i in list1:
    print('%d.%s'%(ii,i))
    ii+=1