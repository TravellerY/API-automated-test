# coding=utf-8
import os
import sys
from tools.handle_excel import HandleExcel
from middleware.config_column import ConfigColumn
from base.request_base import RequestBase
from tools.handle_result import HandleResult
from tools.handle_cookie import HandleCookie
from tools.handle_header import HandleHeader
from tools.handle_log import get_log
import json

# os_path = os.path.abspath(os.path.join(os.getcwd()))
# sys.path.append(os_path)


class RunTest(object):
    def __init__(self):
        self.handle_e = HandleExcel()
        self.config_c = ConfigColumn()
        self.request_b = RequestBase()
        self.handle_r = HandleResult()
        self.handle_c = HandleCookie()
        self.handle_h = HandleHeader()
        self.logger = get_log()

    def run_mian(self):
        data = self.handle_e.get_rows_data()
        for i in data:
            expect_data = None
            cookie_value = None
            get_cookie = None
            header_value = None
            is_run = i[self.config_c.is_run_column()]
            url = i[self.config_c.url_column()]
            method = i[self.config_c.method_column()]
            operating_value = i[self.config_c.operating_data_column()]
            operating_data = json.loads(operating_value)
            is_cookie = i[self.config_c.is_cookie_column()]
            is_header = i[self.config_c.is_header_column()]
            expected_method = i[self.config_c.expected_method_column()]
            expected_value = i[self.config_c.expected_value_column()]
            actual_results = self.config_c.actual_results_column()
            actual_value = self.config_c.actual_value_column()
            excel_row = i[14]
            try:
                if is_run == 'yes':
                    if is_cookie == 'carry':
                        cookie_value = self.handle_c.read_cookie('web')
                    if is_cookie == 'write':
                        get_cookie = {"iscookie": "web"}
                    if is_header == 'yes':
                        header_value = self.handle_h.get_header_data()
                    res = self.request_b.run_mian(method, url, operating_data, cookie_value, get_cookie, header_value)
                    res_code = res["error_code"]
                    if expected_method == 'error_code':
                        if res_code == int(expected_value):
                            self.handle_e.write_value(excel_row, actual_results, 'Pass')
                            self.handle_e.write_value(excel_row, actual_value, res)
                        else:
                            self.handle_e.write_value(excel_row, actual_results, 'Fail')
                            self.handle_e.write_value(excel_row, actual_value, res)
                    if expected_method == 'message':
                        if res_code == expected_value:
                            self.handle_e.write_value(excel_row, actual_results, 'Pass')
                            self.handle_e.write_value(excel_row, actual_value, res)
                        else:
                            self.handle_e.write_value(excel_row, actual_results, 'Fail')
                            self.handle_e.write_value(excel_row, actual_value, res)
                    if expected_method == 'json':
                        if res_code == 0:
                            status = "correctly"
                            expect_data = self.handle_r.get_expect_data(url, status)
                        if res_code == 201102:
                            status = 'error'
                            expect_data = self.handle_r.get_expect_data(url, status)
                        res_data = self.handle_r.result_comparison(res, expect_data)
                        if res_data:
                            self.handle_e.write_value(excel_row, actual_results, 'Pass')
                            self.handle_e.write_value(excel_row, actual_value, res)
                        else:
                            self.handle_e.write_value(excel_row, actual_results, 'Fail')
                            self.handle_e.write_value(excel_row, actual_value, res)
                    self.logger.debug(f"method{method}，URL{url}，data{operating_value}，最终结果{res}")
            except Exception as e:
                print("接口执行失败")
                raise e


if __name__ == '__main__':
    run_test = RunTest()
    run_test.run_mian()
