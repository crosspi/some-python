import time
import requests
import ctypes
import os


def find(find_path):
    for i in ["bing", "random"]:
        list_time = []
        for find_file in os.listdir(find_path):
            if i in find_file:
                ctime = os.path.getctime(os.path.join(find_path, find_file))
                list_time.append(ctime)

        list_time.sort(reverse=True)
        delete_time = list_time[0:5]
        for find_file in os.listdir(find_path):
            if i in find_file:
                if os.path.getctime(os.path.join(find_path, find_file)) not in delete_time:
                    os.remove(os.path.join(find_path, find_file))


def find_dir():
    dir_path = os.path.expanduser('~') + r"\Desktop\images"
    if os.path.exists(dir_path):
        pass
    else:
        os.makedirs(dir_path)
    return dir_path


path = find_dir()


def url():
    url_bing = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN'
    a = requests.get(url=url_bing)
    dict1 = eval(a.text, {'true': 'True'})
    dict2 = dict1.get('images')
    dict3 = dict2[0]
    dict4 = dict3.get('url')
    images_url = 'http://cn.bing.com' + dict4
    return images_url


def wt(url_images):
    ti = time.gmtime()
    if url_images == 'https://bing.icodeq.com':
        ti = time.strftime('%Y-%m-%d-%H%M%S')
        ti = 'randomimages' + ti
    else:
        ti = time.strftime('%Y-%m-%d')
        ti = 'bingimages' + ti
    data = requests.get(url=url_images)
    fd4 = open(path + r'/%s.jpg' % ti, 'wb')
    fd4.write(data.content)
    fd4.close()
    return ti + '.jpg'


def change_bing():  # 存放图片文件的文件夹路径
    # img_lst = os.listdir(path=path)  # 获取文件夹下的所有图片，并存放在列表
    # file = random.choice(img_lst)    # 随机选择图片
    images_url = url()
    file = wt(url_images=images_url)
    img_path = os.path.join(path, file)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img_path, 0)
    find(path)


def change_random():  # 存放图片文件的文件夹路径
    # img_lst = os.listdir(path=path)  # 获取文件夹下的所有图片，并存放在列表
    # file = random.choice(img_lst)    # 随机选择图片
    file = wt(url_images='https://bing.icodeq.com')
    img_path = os.path.join(path, file)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img_path, 0)
    find(path)
