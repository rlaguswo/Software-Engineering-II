import unittest
from credit_card_validator import credit_card_validator


class Testcase(unittest.TestCase):
    # Empty String
    def test1(self):
        self.assertFalse(credit_card_validator(""))

    # Visa: Correct Prefix: 4, Correct checksum, Correct Length: 16
    def test2(self):
        a = 4272958506656125
        self.assertTrue(credit_card_validator(str(a)))

    # American Express:
    # Correct Prefix: 37, Correct checksum, Correct Length: 15
    def test3(self):
        a = 370008428310150
        self.assertTrue(credit_card_validator(str(a)))

    # Master Card: Correct Prefix: 2720, Correct checksum, Correct Length: 16
    def test4(self):
        a = 2720272027202720
        self.assertTrue(credit_card_validator(str(a)))

    # Visa: Correct Prefix: 4, Correct checksum, wrong length:15
    def test5(self):
        a = 450131652221134
        self.assertFalse(credit_card_validator(str(a)))

    # American Express: Prefix: 34, Correct checksum, wrong Length: 16
    def test6(self):
        a = 3498651253577863
        self.assertFalse(credit_card_validator(str(a)))

    # Master Card: Prefix: 55, Correct Length: 16, Wrong Checksum
    def test7(self):
        a = 5372076155746456
        self.assertTrue(credit_card_validator(str(a)))


if __name__ == '__main__':
    unittest.main()
