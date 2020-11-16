import unittest
from src.sample.zad2 import *
from parameterized import parameterized, parameterized_class


class PasswordParameterizedPackage(unittest.TestCase):

    @parameterized.expand([
        ("", False),
        ("AaBbCc123#", True),
        ("ABc12#", False),
        ("aabbcc123#", False),
        ("AaBbCc#&$", False),
        ("AaBbCc123", False),
    ])
    def test_one_parameterized_tests(self, pwd, exp):
        self.assertEqual(self.password.ValidPassword(pwd), exp)

    @parameterized.expand([
        (2115, TypeError),
        ([], TypeError),
    ])
    def test_one_parameterized_raises(self, inp, exp):
        self.assertRaises(exp, self.password.ValidPassword, inp)

    def setUp(self):
        self.password = Password()


if __name__ == '__main__':
    unittest.main()
