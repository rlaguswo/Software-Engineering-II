import unittest

from tasks import conv_endian


class TestCase(unittest.TestCase):
    # test function returns 0 into hexadecimal bytes
    def test_default_big_endian_0(self):
        self.assertEqual(conv_endian(0), "00")

    # test function return the number in big endian without writing 'big'.
    def test_default_big_endian_954786(self):
        self.assertEqual(conv_endian(954786), "0E 91 A2")

    # test function return the negative number in big endian without writing 'big'.
    def test_default_big_endian_neg_964786(self):
        self.assertEqual(conv_endian(-954786), "-0E 91 A2")

    # test function return the number in big endian with writing 'big'
    def test_big_endian_954786(self):
        self.assertEqual(conv_endian(954786, 'big'), "0E 91 A2")

    # test function return the negative number in big endian with writing 'big'
    def test_big_endian_neg_954786(self):
        self.assertEqual(conv_endian(-954786, 'big'), "-0E 91 A2")

    # test function returns the number in little endian with writing 'little
    def test_little_endian_954786(self):
        self.assertEqual(conv_endian(954786, 'little'), "A2 91 0E")

    # test function returns the negative number in little endian with writing 'little
    def test_little_endian_neg_954786(self):
        self.assertEqual(conv_endian(-954786, 'little'), "-A2 91 0E")

    # test function returns non if we write endian which is not 'little' or 'big
    def test_other_value_of_endian_954786(self):
        self.assertEqual(conv_endian(954786, 'smallest'), None)


if __name__ == '__main__':
    unittest.main()
