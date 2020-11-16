import unittest
from src.sample.zad3 import *
from parameterized import parameterized


class PlanetsParameterizedPackage(unittest.TestCase):
    @parameterized.expand([
        (2134835688, "Merkury", 280.88),
        (1234567890, "Wenus", 63.59),
        (7894561230, "Mars", 133.01),
        (9517538426, "Jowisz", 25.42),
        (842675931, "Saturn", 0.91),
        (3216549870, "Uran", 1.21),
        (9876543215, "Neptun", 1.9),
        (1000000000, "Ziemia", 31.69),

    ])
    def test_parameterized_tests(self, num, name, exp):
        self.assertEqual(self.temp.game(num, name), exp)

    @parameterized.expand([
        ("milion", "Ziemia", Exception),
        (1000000000, 78.1, Exception),
        (456546456385, "", Exception),
        (None, "Jowisz", Exception),
        (78946545, None, Exception),
        (None, None, Exception),
        (879352463365, "Europa", Exception),
        (0, "Ziemia", Exception)
    ])
    def test_parameterized_rises(self, inp1, inp2, exp):
        self.assertRaises(exp, self.temp.game, inp1, inp2)

    def setUp(self):
        self.temp = Planets()


if __name__ == '__main__':
    unittest.main()
