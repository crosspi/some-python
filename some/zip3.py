import itertools
import zipfile
from concurrent.futures import ThreadPoolExecutor


def extract(file, password):
    if not flag:
        return
    file.extractall(path='..', pwd=''.join(password).encode('utf-8'))


def result(f):
    exception = f.exception()
    if not exception:
        # 如果获取不到异常说明破解成功
        print('密码为：', f.pwd)
        global flag
        flag = False


if __name__ == '__main__':
    # 创建一个标志用于判断密码是否破解成功
    flag = True
    # 创建一个线程池
    pool = ThreadPoolExecutor(100)
    nums = [str(i) for i in range(10)]
    chrs = [chr(i) for i in range(65, 91)]
    # 生成数字+字母的6位数密码
    password_lst = itertools.permutations(nums + chrs, 4)
    # 创建文件句柄
    zfile = zipfile.ZipFile(
        r"C:\Users\86138\Downloads\Compressed\pycharm.zip", 'r')
    for pwd in password_lst:
        if not flag:
            break
        f = pool.submit(extract, zfile, pwd)
        f.pwd = pwd
        f.pool = pool
        f.add_done_callback(result)
