import requests


def api_history():
    url = "https://api.ahfi.cn/api/lsjt?format=json"

    payload = {}
    headers = {
        'Cache-Control': 'no-cache',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive'
    }
    response = requests.request("GET", url, headers=headers, data=payload)

    text = response.text
    history = text
    history = eval(history)
    print('今天是:%s' % history.get('day'))
    print('历史上的今天发生了:')
    list1 = history.get('content')
    ii = 1
    for i in list1:
        print('%d.%s' % (ii, i))
        ii += 1


def api_ip():
    # 'https://api.ahfi.cn/api/p?type=' is not do
    ip_url = requests.get(url='https://api.ahfi.cn/api/bip')
    ip = ip_url.text
    print('ip地址为%s' % ip)


def api_translation():
    wz = input('请输入文字:')
    if wz:
        pass
    else:
        wz = '文字'
    hh = requests.get(url='https://api.ahfi.cn/api/trans?text=%s' % wz)
    hh = eval(hh.text)
    print(hh.get('content'))


def api_weibo():
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
        print(i + 1, re[i].get('name'))
        print('热度:', re[i].get('hot'))
        print('网址:', re[i].get('url'))


def api_yl():
    url = requests.get('https://api.ahfi.cn/api/nlrq?')
    re = eval(url.text)
    v = 1
    for value in re.values():
        if v == 1 or v == 2:
            pass
        else:
            print(value)
        v += 1


if __name__ == '__main__':
    print("请选择")
