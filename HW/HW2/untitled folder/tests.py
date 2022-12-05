import unittest
from contrived_func import contrived_func


class Testcase(unittest.TestCase):

    def test1(self):
        a = 130
        self.assertTrue(contrived_func(a))

    def test2(self):
        a = 55
        self.assertFalse(contrived_func(a))

    def test3(self):
        a = 150
        self.assertFalse(contrived_func(a))

    def test4(self):
        a = 0
        self.assertTrue(contrived_func(a))

    def test5(self):
        a = 6
        self.assertFalse(contrived_func(a))

    def test6(self):
        a = 1001
        self.assertFalse(contrived_func(a))

    def test7(self):
        a = 48
        self.assertFalse(contrived_func(a))


if __name__ == '__main__':
    unittest.main()
