import requests
ip_url = requests.get(url='https://api.ahfi.cn/api/bip')
ip = ip_url.text
ip_inquire = 'https://api.ahfi.cn/api/ip?type='+ip
ip_xx = requests.get(url=ip_inquire)
dict1 = eval(ip_xx.text, {'true': 'True'})
dict2 = dict1.get('site')
print('ip地址为%s' % ip)
print('省份是:%s' % dict2.get('province'))
print('市区是:%s' % dict2.get('city'))
print('邮编是:%s' % dict2.get('adcode'))
dict3 = dict1.get('weather')
print('天气是:%s' % dict3.get('weather'))
print('温度是:%s度' % dict3.get('temperature'))
