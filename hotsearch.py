import requests
import time
import pandas
ti = time.gmtime()
ti = time.strftime('%Y-%m-%d-%H%M%S')
print('现在时间为:%s' % ti)


def hotsearch_get(url, hot):
    for a in (0, 20):
        re = requests.get(url=url).text
        re = eval(re)
        code = int(re.get('code'))
        if code == 1502:
            time.sleep(6)
            continue
        if code == 200:
            re = re.get('data')
            re = re.get('result')
            print(hot)
            re = pandas.Series(re)
            re.index = re.index+1
            print(re)
            # for i in range(len(re)):
            #     print(i+1, re[i])
            break


hotsearch_get(
    'http://s.api.enetapi.com/api/WeiboHotSearch?hot=rt&qty=20 ', '微博热搜')
hotsearch_get(
    'http://s.api.enetapi.com/api/BaiduHotSearch?hot=rt&qty=20 ', '百度热搜')
hotsearch_get(
    'http://s.api.enetapi.com/api/ZhihuHotSearch?hot=rt&qty=20 ', '知乎热搜')
hotsearch_get(
    'http://s.api.enetapi.com/api/ToutiaoHotsearch?hot=rt&qty=20 ', '头条热搜')
hotsearch_get(
    'http://s.api.enetapi.com/api/TikTokHotSearch?hot=rt&qty=20 ', '抖音热搜')
hotsearch_get(
    'http://s.api.enetapi.com/api/SogouHotSearch?hot=rt&qty=10 ', '搜狗热搜')
hotsearch_get(
    'http://s.api.enetapi.com/api/GodhorseHotSearch?hot=rt&qty=20 ', '神马热搜')
time.sleep(4)
hotsearch_get(
    'http://s.api.enetapi.com/api/360HotSearch?hot=rt&qty=20 ', '360热搜')
