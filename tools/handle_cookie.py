# coding=utf-8
import os
import sys

os_path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os_path)
from tools.handle_json import HandleJson
import json


class HandleCookie(object):
    def __init__(self):
        file_name = os.path.join(os.path.dirname(os.path.dirname(__file__)), r'config/cookies.json')
        self.hand_j = HandleJson(file_name)

    def read_cookie(self, cookie_key):
        """
        根据关键字读取cookies.json文件的值
        :param cookie_key:
        :return:
        """
        cookie_value = self.hand_j.get_data(cookie_key)
        return cookie_value

    def write_cookie(self, value, cookie_key):
        data = self.hand_j.load_json()
        data[cookie_key] = value
        self.hand_j.write_value(data)

# if __name__ == '__main__':
#     hand_c = HandleCookie()
#     data = {
#         "aaa": "2313123123123123123123",
#         "ccc":"231easedasdasdasd"
#     }
#     hand_c.write_cookie(data, "web")
#     res = hand_c.read_cookie("web")
#     print(res)
