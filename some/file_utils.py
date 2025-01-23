"""
文件操作工具模块
包含文件搜索和重命名功能
"""

import os
import time


class FileSearcher:
    """文件搜索类"""

    def __init__(self, search_path=None, file_types=None):
        """
        初始化文件搜索器
        :param search_path: 搜索路径，默认为当前目录
        :param file_types: 文件类型列表，如['.txt', '.csv']
        """
        self.search_path = search_path or os.getcwd()
        self.file_types = file_types
        self.found_files = []

    def search_files(self):
        """搜索指定类型的文件"""
        if not self.file_types:
            self.file_types = input('请输入要搜索的文件类型，用逗号隔开:').split(',')

        self.found_files = []
        for filename in os.listdir(self.search_path):
            if any(filename.endswith(ext) for ext in self.file_types):
                self.found_files.append(filename)

        print(f"找到的文件: {self.found_files}")
        return self.found_files

    def rename_file(self, filename, prefix='hotsearch'):
        """
        重命名文件并添加时间戳
        :param filename: 要重命名的文件名
        :param prefix: 文件名前缀，默认为'hotsearch'
        :return: 新文件名
        """
        timestamp = time.strftime('%Y-%m-%d %H%M%S')
        new_name = f"{prefix}_{timestamp}{os.path.splitext(filename)[1]}"
        os.rename(
            os.path.join(self.search_path, filename),
            os.path.join(self.search_path, new_name)
        )
        return new_name
