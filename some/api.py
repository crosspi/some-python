"""
API相关功能模块
包含各种网络API调用
"""

import requests


def api_history():
    """获取历史上的今天事件"""
    url = "https://api.ahfi.cn/api/lsjt?format=json"
    response = requests.get(url)
    history = eval(response.text)

    print('今天是:%s' % history.get('day'))
    print('历史上的今天发生了:')
    for idx, event in enumerate(history.get('content'), 1):
        print(f'{idx}.{event}')


def api_ip():
    """获取当前IP地址"""
    ip_url = requests.get('https://api.ahfi.cn/api/bip')
    print(f'IP地址为{ip_url.text}')


def api_translation():
    """文本翻译功能"""
    text = input('请输入要翻译的文字:') or '文字'
    response = requests.get(f'https://api.ahfi.cn/api/trans?text={text}')
    translation = eval(response.text)
    print(translation.get('content'))


def api_weibo():
    """获取微博热搜榜"""
    url = "https://tenapi.cn/resou/"
    response = requests.get(url)
    hot_search = eval(response.text).get('list')

    for idx, item in enumerate(hot_search, 1):
        print(f'{idx}. {item.get("name")}')
        print(f'热度: {item.get("hot")}')
        print(f'网址: {item.get("url")}')


def api_yl():
    """获取农历日期"""
    response = requests.get('https://api.ahfi.cn/api/nlrq?')
    lunar_data = eval(response.text)

    # 跳过前两个值（状态码和消息）
    for value in list(lunar_data.values())[2:]:
        print(value)
