# coding=utf-8
import os
import sys
os_path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os_path)
from tools.handle_json import HandleJson
from deepdiff import DeepDiff




class HandleResult(object):
    def __init__(self):
        self.handle_j = HandleJson()

    def get_expect_data(self, key, status):
        result_all = self.handle_j.get_data(key)
        result_status = result_all.get(status)
        return result_status

    def result_comparison(self, dict1, dict2):
        if isinstance(dict1, dict) and isinstance(dict2, dict):
            result = DeepDiff(dict1, dict2, ignore_order=False).to_dict()
            # print(result)
            if result.get('dictionary_item_removed'):
                return False
            else:
                return True

#
# if __name__ == '__main__':
#     dict1 = {"aaa12": "bbb", "aaa1": "ccc"}
#     dict2 = {"aaa12": "bbb1", "aaa1": "ccc1"}
#     handle_r = HandleResult()
#     result = handle_r.result_comparison(dict1, dict2)
#     print(result)
