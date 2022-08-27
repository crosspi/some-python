import time

a = time.time()


class A:
    def __init__(self, my, your):
        self.my = my
        self.your = your
        self.width = 5
        self.height = 5

    def p(self):
        print(self.my, self.your, self.width, self.height)

    @classmethod
    def go(cls):
        print('ppppp')

    @staticmethod
    def gu():
        print(7777)


class B(A):
    def __int__(self):
        super.__init__(A)


if __name__ == '__main__':
    AA = B(my='lll', your='pppp')
    AA.p()
    AA.go()
    A.gu()
