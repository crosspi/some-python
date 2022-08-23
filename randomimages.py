import requests
import time
import win32api
import win32con
import win32gui
import os                 # 用于文件夹操作
images_url = 'https://bing.icodeq.com'


def wt(url_images):
    ti = time.gmtime()
    ti = time.strftime('%Y-%m-%d-%H%M%S')
    ti = 'bingimages'+ti
    data = requests.get(url=url_images)
    fd4 = open(r'C:/Users/86138/Desktop/images/%s.jpg' % ti, 'wb')
    fd4.write(data.content)
    fd4.close()
    return ti


def window_screem(img_path):                # img_path 作为壁纸图片的路径
    key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,
                              'Control panel\\Desktop', 0, win32con.KEY_SET_VALUE)
    # 打开注册表，并指定对子项的操作，在更改注册表内容时，一定要先打开注册表
    win32api.RegSetValueEx(key, 'wapaperStyle', 0, win32con.REG_SZ, '2')
    # key 表示对哪一个子项修改值，'wapaperStyle'是指壁纸类型，0表示桌面居中，win32con.REG_SZ是数据的类型，2代表拉伸
    win32api.RegSetValueEx(key, "Tilewallpaper", 0, win32con.REG_SZ, "0")
    # 设置背景风格，0 为平铺
    win32gui.SystemParametersInfo(
        win32con.SPI_SETDESKWALLPAPER, img_path, win32con.SPIF_SENDWININICHANGE)
    # 刷新屏幕


def change_wapaer(path):             # 存放图片文件的文件夹路径
    # img_lst = os.listdir(path=path)  # 获取文件夹下的所有图片，并存放在列表
    # file = random.choice(img_lst)    # 随机选择图片
    ti = wt(url_images=images_url)
    file = ti+'.jpg'
    img_path = os.path.join(path, file)
    print(img_path)
    window_screem(img_path)
    print('完成')


if __name__ == '__main__':
    change_wapaer(r'C:/Users/86138/Desktop/images')  # 存放图片的文件夹mport os
