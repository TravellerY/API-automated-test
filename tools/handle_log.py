# coding=utf-8
import os
import sys

os_path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os_path)
import datetime
import logging


def close_handle(func):
    """
    关闭相应的流
    """

    def wrapper():
        func()
        logger.removeHandler(file_handle)
        file_handle.close()

    return wrapper


# @close_handle
def get_log():
    """
    日志文件的操作
    :return:
    """
    file_path = os.path.dirname(os.path.dirname(__file__)) + '/log/'
    file_name = datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
    path = file_path + file_name

    global logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    file_path = os.path.dirname(os.path.dirname(__file__)) + '/log/'
    file_name = datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
    path = file_path + file_name

    global file_handle
    file_handle = logging.FileHandler(path, 'a', encoding='utf-8')
    file_handle.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)4s - %(name)4s - %(levelname)4s - %(message)s",
                                  datefmt="%Y-%m-%d %H-%M-%S")
    file_handle.setFormatter(formatter)
    logger.addHandler(file_handle)
    return logger

# logger = get_log()
# logger.debug("moss")
