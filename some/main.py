"""
主程序入口
整合了图片下载、壁纸设置、文件搜索、API调用等功能
"""

from images import change_bing, change_random
from api import api_history, api_ip, api_translation, api_weibo, api_yl
from file_utils import FileSearcher


def main():
    print("请选择功能：")
    print("1. 设置必应每日壁纸（1080p）")
    print("2. 设置必应每日壁纸（4K）")
    print("3. 设置随机壁纸（1080p）")
    print("4. 设置随机壁纸（4K）")
    print("5. 文件搜索")
    print("6. 查看历史上的今天")
    print("7. 查看IP地址")
    print("8. 翻译")
    print("9. 微博热搜")
    print("10. 农历日期")

    choice = input("请输入选项：")

    if choice == "1":
        change_bing('1080p')
    elif choice == "2":
        change_bing('4k')
    elif choice == "3":
        change_random('1080p')
    elif choice == "4":
        change_random('4k')
    elif choice == "5":
        searcher = FileSearcher()
        searcher.search_files()
    elif choice == "6":
        api_history()
    elif choice == "7":
        api_ip()
    elif choice == "8":
        api_translation()
    elif choice == "9":
        api_weibo()
    elif choice == "10":
        api_yl()
    else:
        print("无效选项")


if __name__ == "__main__":
    main()
