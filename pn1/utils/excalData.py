class ExcalVariable(object):
    caseID = 0
    BaseUrl = 2
    interface = 3
    request_data = 4
    expect_value = 5
    result = 8

# Url = BaseUrl + interface


def getCaseID():
    """获取CaseID的列"""
    return ExcalVariable.caseID


def getBaseUrl():
    """获取Url的列"""
    return ExcalVariable.BaseUrl


def getInterface():
    """获取接口的列"""
    return ExcalVariable.interface


def getRequest_data():
    """获取需要请求的数据"""
    return ExcalVariable.request_data


def getExcept_value():
    """获取断言的预期值"""
    return ExcalVariable.expect_value


def getResult():
    """获取断言结果"""
    return ExcalVariable.result