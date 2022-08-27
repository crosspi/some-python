import os


class F:
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


if __name__ == '__main__':
    a = F(find_path='C:\my\python\some-python',
          find_types=['.xlsx'])
    F.find(a)
    print(a.list_types)
    print(a.find_types)
