# coding=utf=8
import os
import sys
os_path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os_path)
import configparser




class HandleIni(object):
    def __init__(self, file_name=None):
        """
        构造函数
        :param file_name: 文件地址
        """
        if file_name is None:
            self.file_name = os.path.join(os.path.dirname(os.path.dirname(__file__)), r'config/deploy.ini')
        else:
            self.file_name = file_name

    def load_ini(self):
        """
        加载配置文件
        :return:
        """
        cf = configparser.ConfigParser()
        cf.read(self.file_name, encoding='UTF-8')
        return cf

    def get_value(self, key, node=None):
        """
        获取配置文件中响应的值
        :param node: 文件中内容的标签
        :param key: 相应值所对应的关键字
        :return:
        """
        if node is None:
            node = 'Server'
        else:
            node = node
        data = self.load_ini().get(node, key)
        return data


# if __name__ == '__main__':
#     handle_i = HandleIni()
#     value = handle_i.get_value(node='Column', key='operating_data')
#     print(value)