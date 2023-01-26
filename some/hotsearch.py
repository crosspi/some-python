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
        if not self.find_types:
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
        after_name = 'hotsearch' + ti + '.csv'
        os.rename(os.path.join(self.find_path, before_name),
                  os.path.join(self.find_path, after_name))
        return after_name


if __name__ == '__main__':
    the_dir = os.getcwd()
    a = F(find_path=the_dir,
          find_types=['.csv'])
    F.find(a)
    csv_name = F.rename(a, a.list_types[0])