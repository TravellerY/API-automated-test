# coding=utf-8
import os
import sys
os_path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os_path)
from tools.handle_excel import HandleExcel
from middleware.config_column import ConfigColumn
from base.request_base import RequestBase
from tools.handle_result import HandleResult
from tools.handle_cookie import HandleCookie
from tools.handle_header import HandleHeader
from tools.handle_log import get_log
from img import HTMLTestRunner
import json
import unittest
import ddt


datas = HandleExcel().get_rows_data()


@ddt.ddt()
class TestRun(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.handle_e = HandleExcel()
        cls.config_c = ConfigColumn()
        cls.request_b = RequestBase()
        cls.handle_r = HandleResult()
        cls.handle_c = HandleCookie()
        cls.handle_h = HandleHeader()
        cls.logger = get_log()

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()

    @ddt.data(*datas)
    def test_all_case(self, data):
        expect_data = None
        cookie_value = None
        get_cookie = None
        header_value = None
        is_run = data[self.config_c.is_run_column()]
        url = data[self.config_c.url_column()]
        method = data[self.config_c.method_column()]
        operating_value = data[self.config_c.operating_data_column()]
        operating_data = json.loads(operating_value)
        is_cookie = data[self.config_c.is_cookie_column()]
        is_header = data[self.config_c.is_header_column()]
        expected_method = data[self.config_c.expected_method_column()]
        expected_value = data[self.config_c.expected_value_column()]
        actual_results = self.config_c.actual_results_column()
        actual_value = self.config_c.actual_value_column()
        excel_row = data[14]
        try:
            if is_run == 'yes':
                if is_cookie == 'carry':
                    cookie_value = self.handle_c.read_cookie('web')
                if is_cookie == 'write':
                    get_cookie = {"iscookie": "web"}
                if is_header == 'yes':
                    header_value = self.handle_h.get_header_data()
                res = self.request_b.run_mian(method, url, operating_data, cookie_value, get_cookie, header_value)
                self.logger.debug(f"method:{method}，URL:{url}，data:{operating_value}，最终结果:{res}")
                res_code = res["error_code"]
                if expected_method == 'error_code':
                    self.assertEqual(res_code, int(expected_value))
                    self.handle_e.write_value(excel_row, actual_results, 'Pass')
                    self.handle_e.write_value(excel_row, actual_value, res)
                if expected_method == 'message':
                    self.assertEqual(res_code, expected_value)
                    self.handle_e.write_value(excel_row, actual_results, 'Pass')
                    self.handle_e.write_value(excel_row, actual_value, res)
                if expected_method == 'json':
                    if res_code == 0:
                        status = "correctly"
                        expect_data = self.handle_r.get_expect_data(url, status)
                    if res_code == 201102:
                        status = 'error'
                        expect_data = self.handle_r.get_expect_data(url, status)
                    res_data = self.handle_r.result_comparison(res, expect_data)
                    print(res_data)

                    self.assertTrue(res_data)
                    self.handle_e.write_value(excel_row, actual_results, 'Pass')
                    self.handle_e.write_value(excel_row, actual_value, res)
        except Exception as e:
            self.handle_e.write_value(excel_row, actual_results, 'Fail')
            self.handle_e.write_value(excel_row, actual_value, res)
            raise e

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()


if __name__ == '__main__':
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), r'report/API测试报告.html')
    case_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), r'run_main')
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test_unittest_*.py")
    with open(file_path, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="聚合网接口测试", description="测试流程如下")
        runner.run(discover)

    # testsuit = unittest.TestSuite()
    # testsuit.addTest(TestRun('test_all_case'))
    # fp = open(file_path, 'w')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'聚合接口测试', description=u'用例执行情况：')
    # runner.run(testsuit)
    # fp.close()
