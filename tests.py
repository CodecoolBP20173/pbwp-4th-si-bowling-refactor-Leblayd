import unittest
from bowling import score


class MyTests(unittest.TestCase):
    def test_gutter_game(self):
        self.assertEqual(score("--------------------"),  0)

    def test_all_ones(self):
        self.assertEqual(score("11111111111111111111"),  20)

    def test_one_spare(self):
        self.assertEqual(score("5/3-----------------"),  16)

    def test_roll_strike(self):
        self.assertEqual(score("X34----------------"),   24)

    def test_perfect_game(self):
        self.assertEqual(score("XXXXXXXXXXXX"),          300)

    def test_case_sensitivity(self):
        self.assertEqual(score("XXxxxXXXXxXx"),          300)

    def test_everything_is_fine_please(self):
        self.assertEqual(score("11111111112222222222"), 30)
        self.assertEqual(score("5/11------------3/11"), 26)
        self.assertEqual(score("1/35XXX458/X3/23"),     160)
        self.assertEqual(score("1/35XXX458/X3/XX6"),    189)


if __name__ == '__main__':
    unittest.main()
