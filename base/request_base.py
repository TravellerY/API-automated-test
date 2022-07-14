# coding='utf-8'
import os
import sys

os_path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os_path)
import requests
import json
from tools.handle_ini import HandleIni
from tools.handle_cookie import HandleCookie


class RequestBase(object):
    def __init__(self):
        self.handle_i = HandleIni()
        self.handle_c = HandleCookie()

    def request_get(self, url, data, cookie_value=None, header_value=None):
        """
        get请求方式封装
        :param header_value:
        :param cookie_value:
        :param url: url地址
        :param data: 操作的数据
        :return:
        """
        res = requests.get(url, params=data, cookies=cookie_value, headers=header_value, verify=False)
        return res

    def request_post(self, url, data, cookie_value=None, header_value=None):
        """
        post请求方式封装
        :param header_value:
        :param cookie_value:
        :param url: URL地址
        :param data: 操作的数据
        :return:
        """
        res = requests.post(url, data=data, cookies=cookie_value, headers=header_value, verify=False)
        return res

    def run_mian(self, method, url, data, cookie_value=None, get_cookie=None, header_value=None):
        """

        :param header_value:
        :param get_cookie:
        :param cookie_value:
        :param method:
        :param url:
        :param data:
        :return:
        """
        host = self.handle_i.get_value('host')
        host_url = host + url
        if method == 'get':
            response = self.request_get(host_url, data, cookie_value, header_value)
            if get_cookie:
                cookie_value_jar = response.cookies
                cookie_data = requests.utils.dict_from_cookiejar(cookie_value_jar)
                coojie_key = get_cookie['iscookie']
                self.handle_c.write_cookie(cookie_data, coojie_key)
            res = self.request_get(host_url, data, cookie_value).text
        if method == 'post':
            response = self.request_post(host_url, data, cookie_value, header_value)
            if get_cookie:
                cookie_value_jar = response.cookies
                cookie_data = requests.utils.dict_from_cookiejar(cookie_value_jar)
                coojie_key = get_cookie['iscookie']
                self.handle_c.write_cookie(cookie_data, coojie_key)
            res = self.request_post(host_url, data, cookie_value).text

        try:
            res = json.loads(res)
        except Exception:
            print('该返回值无法转换为JSON格式')
            raise Exception
        return res

# if __name__ == '__main__':
#     url = '/mobile/get'
#     data = {"phone": 17323119716, "dtype": "json", "key": "39fcc171d1ee07887e8fe34ea5b40789"}
#     method = 'post'
#     request_b = RequestBase()
#     res = request_b.run_mian(method, url, data)
#     print(res)
