import os
import time

import pandas
import requests


class F():
    def __init__(self, find_path, find_types):
        self.find_types = find_types
        self.list_types = []
        self.find_path = find_path

    def find(self):
        if self.find_types == []:
            self.find_types = input('请输入搜索文件类型,用逗号隔开:').split(',')
        self.list_types = []
        find_dir = os.listdir(path=self.find_path)
        for i in find_dir:
            for ii in self.find_types:
                if ii == os.path.splitext(i)[1]:
                    self.list_types.append(i)

    def rename(self, before_name):
        ti = time.gmtime()
        ti = time.strftime('%Y-%m-%d %H%M%S')
        after_name = 'hotsearch' + ti + '.xlsx'
        os.rename(os.path.join(self.find_path, before_name),
                  os.path.join(self.find_path, after_name))
        return after_name


if __name__ == '__main__':
    a = F(find_path='C:\my\python\some-python',
          find_types=['.xlsx'])
    F.find(a)
    xlsx_name = F.rename(a, a.list_types[0])


def hotsearch_get(url):
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
            re = list(re)
            return re

            break


re1 = hotsearch_get(
    'http://s.api.enetapi.com/api/WeiboHotSearch?hot=rt&qty=20 ')
re2 = hotsearch_get(
    'http://s.api.enetapi.com/api/BaiduHotSearch?hot=rt&qty=20 ')
re3 = hotsearch_get(
    'http://s.api.enetapi.com/api/ZhihuHotSearch?hot=rt&qty=20 ')
time.sleep(6)
re4 = hotsearch_get(
    'http://s.api.enetapi.com/api/ToutiaoHotsearch?hot=rt&qty=20 ')
re5 = hotsearch_get(
    'http://s.api.enetapi.com/api/TikTokHotSearch?hot=rt&qty=20 ')
re7 = hotsearch_get(
    'http://s.api.enetapi.com/api/GodhorseHotSearch?hot=rt&qty=20 ')
time.sleep(6)
re8 = hotsearch_get(
    'http://s.api.enetapi.com/api/360HotSearch?hot=rt&qty=20 ')
res = list(zip(re1, re2, re3, re4, re5, re7, re8))
columns = ['微博', '百度', '知乎', '头条', '抖音', '神马', '360']
df = pandas.DataFrame(data=res, columns=columns)
df.index += 1
xlsx_path = 'C:\my\python\some-python' + '\\' + xlsx_name
df.to_excel(xlsx_path)
print('完成')
