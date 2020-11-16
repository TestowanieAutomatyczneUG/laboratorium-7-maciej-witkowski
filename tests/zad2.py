import unittest
from src.sample.zad2 import *
from parameterized import parameterized, parameterized_class
from nose.tools import assert_equal, assert_raises


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


@parameterized_class(('pwd', 'exp'), [
    ("", False),
    ("AaBbCc123#", True),
    ("ABc12#", False),
    ("aabbcc123#", False),
    ("AaBbCc#&$", False),
    ("AaBbCc123", False),
])
class PasswordParameterizedPackage2Tests(unittest.TestCase):
    def test_second_parameterized_tests(self):
        self.assertEqual(self.password.ValidPassword(self.pwd), self.exp)

    def setUp(self):
        self.password = Password()


@parameterized_class(('inp', 'exp'), [
    (2115, TypeError),
    ([], TypeError),
])
class PasswordParameterizedPackage2Raises(unittest.TestCase):
    def test_second_parameterized_raises(self):
        self.assertRaises(self.exp, self.password.ValidPassword, self.inp)

    def setUp(self):
        self.password = Password()


@parameterized([
    ("", False),
    ("AaBbCc123#", True),
    ("ABc12#", False),
    ("aabbcc123#", False),
    ("AaBbCc#&$", False),
    ("AaBbCc123", False),
])
def test_third_parameterized_tests(pwd, exp):
    password = Password()
    assert_equal(password.ValidPassword(pwd), exp)


@parameterized([
    (2115, TypeError),
    ([], TypeError),
])
def test_third_parameterized_raises(inp, exp):
    password = Password()
    assert_raises(exp, password.ValidPassword, inp)


if __name__ == '__main__':
    unittest.main()
