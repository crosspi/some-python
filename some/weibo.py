import requests

url = "https://tenapi.cn/resou/"

payload = {}
headers = {
    'Cache-Control': 'no-cache',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive'
}

response = requests.request("GET", url, headers=headers, data=payload)

re = response.text
re = eval(re)
re = re.get('list')
print(re)
for i in range(0, len(re)):
    print(i+1, re[i].get('name'))
    print('热度:', re[i].get('hot'))
    print('网址:', re[i].get('url'))
