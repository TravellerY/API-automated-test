import os
import sys
os_path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os_path)

import json



class HandleJson(object):
    def __init__(self, file_name=None):
        """
        构造函数
        :param file_name: json文件的地址信息
        """
        if file_name is None:
            self.file_name = os.path.join(os.path.dirname(os.path.dirname(__file__)), r'config/response_data.json')
        else:
            self.file_name = file_name

    def load_json(self):
        """
        加载并读取JSON文件中的所有值
        :return:
        """
        with open(self.file_name, 'r', encoding='utf-8') as f:
            data = f.read()
            return json.loads(data)

    def get_data(self, key):
        """
        根据key值获取相应的value
        :param key: 关键字
        :return:
        """
        data = self.load_json().get(key)
        return data

    def write_value(self, value):
        """
        向json文件中写入数据
        :return:
        """
        value = json.dumps(value)
        with open(self.file_name, 'w', encoding='utf-8') as f:
            f.write(value)


# if __name__ == '__main__':
#     handle_j = HandleJson()
#     data = handle_j.get_data("/mobile/get")
#     data1 = data.get('error')
#     # data = handle_j.load_json()
#     print(data1)

    # print(type(data))
