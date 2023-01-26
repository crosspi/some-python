import os
import time
import requests
import ctypes


def url():
    url_bing = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN'
    a = requests.get(url=url_bing)
    dict1 = eval(a.text, {'true': 'True'})
    dict2 = dict1.get('images')
    dict3 = dict2[0]
    dict4 = dict3.get('url')
    images_url = 'http://cn.bing.com' + dict4
    return images_url


def wt_bing(url_images):
    ti = time.gmtime()
    ti = time.strftime('%Y-%m-%d')
    ti = 'bingimages' + ti
    data = requests.get(url=url_images)
    fd4 = open(r'C:/Users/15302/Desktop/images/%s.jpg' % ti, 'wb')
    fd4.write(data.content)
    fd4.close()
    return ti


def wt_random(url_images):
    ti = time.gmtime()
    ti = time.strftime('%Y-%m-%d-%H%M%S')
    ti = 'bingimages' + ti
    data = requests.get(url=url_images)
    fd4 = open(r'C:/Users/15302/Desktop/images/%s.jpg' % ti, 'wb')
    fd4.write(data.content)
    fd4.close()
    return ti


def window_screem(img_path):  # img_path 作为壁纸图片的路径
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img_path, 0)


def change_bing(path):  # 存放图片文件的文件夹路径
    # img_lst = os.listdir(path=path)  # 获取文件夹下的所有图片，并存放在列表
    # file = random.choice(img_lst)    # 随机选择图片
    images_url = url()
    ti = wt_bing(url_images=images_url)
    print('图片下载完成')
    file = ti + '.jpg'
    img_path = os.path.join(path, file)
    print(img_path)
    window_screem(img_path)


def change_random(path):  # 存放图片文件的文件夹路径
    # img_lst = os.listdir(path=path)  # 获取文件夹下的所有图片，并存放在列表
    # file = random.choice(img_lst)    # 随机选择图片
    ti = wt_random(url_images='https://bing.icodeq.com')
    file = ti + '.jpg'
    img_path = os.path.join(path, file)
    print(img_path)
    window_screem(img_path)
    print('完成')
