import unittest

from deadants import dead_ant_count


# support snake case and camel case functions
def test_dac(ants):
    try:
        return dead_ant_count(ants)
    except NameError:
        return deadAntCount(ants)


class TestDeadAnt(unittest.TestCase):
    def test_basic_cases(self):
        self.assertEqual(test_dac("ant ant ant ant"), 0)
        self.assertEqual(test_dac(""), 0)
        self.assertEqual(test_dac(" "), 0)
        self.assertEqual(test_dac("ant anantt aantnt"), 2)
        self.assertEqual(test_dac("ant ant .... a nt"), 1)
        self.assertEqual(test_dac("ant ant ant ant"), 0)
        self.assertEqual(test_dac(""), 0)
        self.assertEqual(test_dac(" "), 0)
        self.assertEqual(test_dac("ant anantt aantnt"), 2)
        self.assertEqual(test_dac("ant ant .... a nt"), 1)
        self.assertEqual(test_dac("antatn ant ant"), 1)
        self.assertEqual(test_dac("ant a ant anatttt"), 4)
        self.assertEqual(test_dac("antantantan"), 1)
        self.assertEqual(test_dac("aaaaannnntttt"), 5)
        self.assertEqual(test_dac("aaaannnnntttt"), 5)
        self.assertEqual(test_dac("aaaannnnttttt"), 5)
        self.assertEqual(test_dac("a n t"), 1)
        self.assertEqual(test_dac("... .. ..."), 0)
        self.assertEqual(test_dac("$$$ant..a"), 1)
        self.assertEqual(test_dac(".n..tt.n.nt..t.ntant..aaaaa..tn.na.aaat..n..tn.ntan.t"), 10)
        self.assertEqual(test_dac("ant ant .... a nt"), 1)


if __name__ == '__main__':
    unittest.main()
