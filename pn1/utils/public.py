"""
处理文件操作，及其他公共方法的集合
"""
import os


def data_dir(data='data', fileName=None):
    """查找文件路径"""
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), data, fileName)


