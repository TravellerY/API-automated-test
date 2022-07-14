# coding=utf-8
import os
import sys
os_path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os_path)

from tools.handle_ini import HandleIni



class ConfigColumn(object):
    def get_data(self, key, node):
        handle_i = HandleIni()
        get_valeu = int(handle_i.get_value(key, node))
        return get_valeu

    def case_id_column(self):
        """
        测试用例ID 所在列数
        :return:
        """
        column = self.get_data('case_id', 'Column')
        return column

    def is_run_column(self):
        """
        是否执行 所在列数
        :return:
        """
        column = self.get_data('is_run', 'Column')
        return column

    def filenames_column(self):
        """
        前置条件 所在列数
        :return:
        """
        column = self.get_data('filenames', 'Column')
        return column

    def dependent_key_column(self):
        """
        依赖的key 所在列数
        :return:
        """
        column = self.get_data('dependent_key', 'Column')
        return column

    def url_column(self):
        """
        URL 所在列数
        :return:
        """
        column = self.get_data('url', 'Column')
        return column

    def method_column(self):
        """
        接口方式 所在列数
        :return:
        """
        column = self.get_data('method', 'Column')
        return column

    def operating_data_column(self):
        """
        操作数据 所在列数
        :return:
        """
        column = self.get_data('operating_data', 'Column')
        return column

    def is_cookie_column(self):
        """
        cookie操作 所在列数
        :return:
        """
        column = self.get_data('is_cookie', 'Column')
        return column

    def is_header_column(self):
        """
        header操作 所在列数
        :return:
        """
        column = self.get_data('is_header', 'Column')
        return column

    def expected_method_column(self):
        """
        预期结果方式 所在列数
        :return:
        """
        column = self.get_data('expected_method', 'Column')
        return column

    def expected_value_column(self):
        """
        预期结果值 所在列数
        :return:
        """
        column = self.get_data('expected_value', 'Column')
        return column

    def actual_results_column(self):
        """
        实际结果 所在列数
        :return:
        """
        column = self.get_data('actual_results', 'Column')
        return column

    def actual_value_column(self):
        """
        实际结果值 所在列数
        :return:
        """
        column = self.get_data('actual_value', 'Column')
        return column

# if __name__ == '__main__':
#     config_c = ConfigColumn()
#     res = config_c.case_id_column()
#     print(res)
