from ddt import ddt,data,unpack, file_data
import unittest
import time

@ddt
class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('整个测试类开始时执行')

    def setUp(self):
        print('每条测试例都执行')

    # 1-单独传一个参数
    @data(1,2,3)
    def test1(self,a):
        time.sleep(3)
        print('test1',a)
        self.assertEqual(2,a)

    # 2-需要分发参数
    @data((1,2), (2,3))
    @unpack     # 把1分给value1， 2分给value2
    def test2(self, value1, value2):
        time.sleep(3)
        print('test2')
        print(value1, value2)
    #
    # # 3-以列表的方式
    @unpack
    @data([1,2], [3,4],[5,6])
    # 执行3次 1,2   3,4   5,6
    def test3(self, a, b):
        print('test3')
        print(a, b)

    # # 4-以字典格式
    @unpack
    @data({'a':1, 'b':2, },
          {"a":3, 'b':4},
          {"a":5, 'b':'6'}
          )
    def test4(self, a, b):
        print('test4')
        print(a, b)

    # 5以读取文件的形式
    # 可以直接在里面实现参数化
    @file_data(r"C:\Users\zhoujialin\PycharmProjects\vip04\home_work\day4_homework\response_1577700949051.json")
    def test_file(self, *value):
        print(value)

if __name__ == '__main__':
    unittest.main()


