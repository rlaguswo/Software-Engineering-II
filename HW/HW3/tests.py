import random
import unittest
from credit_card_validator import credit_card_validator


class TestCase(unittest.TestCase):
    def test1(self):
        for i in range(0, 1000):
            val = random.randint(10 ** 15, 10 ** 16 - 1)
            credit_card_validator(str(val))

    def test2(self):
        for i in range(0, 1000000):
            val = random.randint(10 ** 14, 10 ** 5 - 1)
            credit_card_validator(str(val))

    def test3(self):
        for i in range(0, 500000):
            val = random.randint(34 * (10 ** 13), 10 ** 15 - 1)
            credit_card_validator(str(val))

    def test4(self):
        for i in range(0, 500000):
            val = random.randint(4 * 10 ** 15, 5 * (10 ** 15) - 1)
            credit_card_validator(str(val))


if __name__ == '__main__':
    unittest.main()
