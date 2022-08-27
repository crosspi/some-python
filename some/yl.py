import requests
url = requests.get('https://api.ahfi.cn/api/nlrq?')
re = eval(url.text)
v = 1
for value in re.values():
    if v == 1 or v == 2:
        pass
    else:
        print(value)
    v += 1
