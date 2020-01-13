"""
动态参数
"""
from pn1.utils.operationJson import OperationJson
from pn1.utils.operationExcal import OperationExcel
import json

operationJson = OperationJson()


def setSo(kd=None):
    """

    :param kd:
    :return:
    """
    # 将str 转换成dict
    test_data = json.loads(operationJson.get_Request_Json(1))
    print(type(test_data))
    test_data['source'] = kd



if __name__ == '__main__':
    setSo()