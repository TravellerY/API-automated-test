# coding=utf-8
import os
import sys
os_path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os_path)
from tools.handle_json import HandleJson



class HandleHeader(object):
    def __init__(self):
        file_name = os.path.join(os.path.dirname(os.path.dirname(__file__)), r'config/header.json')
        self.handle_j = HandleJson(file_name)

    def get_header_data(self):
        """
        获取header.json中的数据
        :return:
        """
        header_data = self.handle_j.load_json()
        return header_data


# if __name__ == '__main__':
#     handle_h = HandleHeader()
#     res = handle_h.get_header_data()
#     print(res)
