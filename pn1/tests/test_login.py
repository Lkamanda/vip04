import unittest
from pn1.base.method import Method, IsAssert
from ddt import ddt, unpack


class JingCai(unittest.TestCase):
    def setUp(self):
        self.obj = Method()
        self.p = IsAssert()

    def statusCode(self, r):
        # 协议状态码
        self.assertEqual(r.status_code, 200)
        # 业务状态码
        self.assertEqual(r.json()['code'], 0)

    def isContent(self, row, r):
        self.statusCode(r=r)
        self.assertTrue(self.p.isContent(row=row, str2=r.text))

    def test_1(self, row):
        r = self.obj.post(row)
        self.isContent(row, r)


