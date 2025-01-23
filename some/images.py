"""
图片处理模块
包含必应壁纸下载、随机壁纸下载、壁纸设置等功能
"""

import os
import time
import requests
import ctypes
import urllib3

# 禁用SSL警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_images_dir():
    """获取图片存储目录，如果不存在则创建"""
    images_dir = os.path.join(os.path.expanduser('~'), 'Desktop', 'images')
    os.makedirs(images_dir, exist_ok=True)
    return images_dir


def download_image(url, prefix='bing', max_retries=3):
    """
    下载图片并保存到指定目录
    :param url: 图片URL
    :param prefix: 文件名前缀
    :param max_retries: 最大重试次数
    :return: 保存的文件名
    """
    images_dir = get_images_dir()
    timestamp = time.strftime(
        '%Y-%m-%d-%H%M%S' if prefix == 'random' else '%Y-%m-%d')
    # 在文件名中加入分辨率信息
    resolution = '4k' if 'uhd' in url else '1080p'
    filename = f"{prefix}_{resolution}_{timestamp}.jpg"
    filepath = os.path.join(images_dir, filename)

    for attempt in range(max_retries):
        try:
            # 禁用SSL验证并设置超时
            response = requests.get(url, verify=False, timeout=10)
            # 检查响应内容是否为图片
            if response.headers.get('Content-Type', '').startswith('image'):
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                return filename
        except requests.exceptions.RequestException as e:
            if attempt == max_retries - 1:
                raise Exception(f"下载图片失败: {str(e)}")
            time.sleep(1)  # 等待1秒后重试

    raise Exception("无法下载图片：达到最大重试次数")


def set_wallpaper(image_path):
    """设置桌面壁纸"""
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)


def clean_old_images(prefix, keep_count=5):
    """
    清理旧图片，保留最新的指定数量
    :param prefix: 图片前缀（'bing'或'random'）
    :param keep_count: 保留的最新图片数量
    """
    images_dir = get_images_dir()
    images = [f for f in os.listdir(images_dir) if f.startswith(prefix)]
    images.sort(key=lambda f: os.path.getctime(
        os.path.join(images_dir, f)), reverse=True)

    for old_image in images[keep_count:]:
        os.remove(os.path.join(images_dir, old_image))


def get_bing_image_url(resolution='1080p'):
    """
    获取必应每日图片URL
    :param resolution: 图片分辨率，可选'1080p'或'4k'
    :return: 图片URL
    """
    if resolution == '1080p':
        return 'https://bing.img.run/1920x1080.php'
    else:
        return 'https://bing.img.run/uhd.php'


def change_bing(resolution='1080p'):
    """
    设置必应每日壁纸
    :param resolution: 图片分辨率，可选'1080p'或'4k'
    """
    image_url = get_bing_image_url(resolution)
    filename = download_image(image_url, 'bing')
    set_wallpaper(os.path.join(get_images_dir(), filename))
    clean_old_images('bing')


def get_random_image_url(resolution='1080p'):
    """
    获取随机壁纸URL
    :param resolution: 图片分辨率，可选'1080p'或'4k'
    :return: 图片URL
    """
    if resolution == '1080p':
        return 'https://bing.img.run/rand.php'
    else:
        return 'https://bing.img.run/rand_uhd.php'


def change_random(resolution='1080p'):
    """
    设置随机壁纸
    :param resolution: 图片分辨率，可选'1080p'或'4k'
    """
    image_url = get_random_image_url(resolution)

    filename = download_image(image_url, 'random')
    set_wallpaper(os.path.join(get_images_dir(), filename))
    clean_old_images('random')
