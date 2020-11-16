import unittest
from src.sample.zad1 import *


class HammingParameterizedFile(unittest.TestCase):
    def test_from_file_tests(self):
        file_tests = open("data/zad1_tests_file")
        for line in file_tests:
            if line.startswith('#'):
                continue
            else:
                data = line.split(',')
                inp1, inp2, res = str(data[0]), str(data[1]), int(data[2].strip('\n'))
                self.assertEqual(self.hamming.distance(inp1, inp2), res)
        file_tests.close()

    def test_from_file_raises(self):
        file_raises = open("data/zad1_raises_file")
        for line in file_raises:
            if line.startswith('#'):
                continue
            else:
                data = line.split(',')
                inp1, inp2, exp = str(data[0]), str(data[1]), str(data[2].strip('\n'))
                self.assertRaises(ValueError, self.hamming.distance, inp1, inp2)
        file_raises.close()

    def setUp(self):
        self.hamming = Hamming()


if __name__ == '__main__':
    unittest.main()
