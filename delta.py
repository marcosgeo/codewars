import unittest

"""
Generators is the point os this kata
"""


def delta(values, level):
    if level > 1:
        values = delta(values, level-1)
    values = iter(values)
    previous = next(values)
    for el in values:
        yield el - previous
        previous = el


class TestDelta(unittest.TestCase):
    def test_delta(self):
        input_list = [1, 2, 4, 7, 11, 16, 22]
        result1 = list(delta(input_list, 1))
        self.assertEqual(result1, [1, 2, 3, 4, 5, 6])
        result2 = list(delta(input_list, 2))
        self.assertEqual(result2, [1, 1, 1, 1, 1])
        self.assertEqual(list(delta(input_list, 3)), [0, 0, 0, 0])
        self.assertEqual(list(delta([3, 3, -5, 77], 2)), [-8, 90])
        print("Everything passed")


if __name__ == "__main__":
    unittest.main()
