import requests
wz = input('请输入文字:')
if wz:
    pass
else:
    wz = '文字'
hh = requests.get(url='https://api.ahfi.cn/api/trans?text=%s' % wz)
hh = eval(hh.text)
print(hh.get('content'))
