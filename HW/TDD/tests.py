import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):
    def test1(self):
        a = ""
        return self.assertFalse(check_pwd(a))
    #check password has lower cases.
    def test2(self):
        a = "12345678"
        return self.assertFalse(check_pwd(a))
    #Check upper case
    def test3(self):
        a = "12345678a"
        return self.assertFalse(check_pwd(a))
    #check digits
    def test4(self):
        a = "aAbBaafsd"
        return self.assertFalse(check_pwd(a))
    #check symbols
    def test5(self):
        a = "aA12345678"
        return self.assertFalse(check_pwd(a))
    #check the valid password
    def test6(self):
        a = "aAB1234~`!@+"
        return self.assertTrue(check_pwd(a))
if __name__ == '__main__':
    unittest.main()
