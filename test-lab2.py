import unittest
from lab2 import min_time_to_paint


class TestMinTimeToPaint(unittest.TestCase):

    def test_basic_case(self):
        self.assertEqual(min_time_to_paint(3, 10, [17, 18, 19, 20, 21]), 390)

    def test_same_length(self):
        self.assertEqual(min_time_to_paint(2, 5, [10, 10, 10, 10]), 100)

    def test_one_board(self):
        self.assertEqual(min_time_to_paint(1, 5, [10]), 50)

    def test_one_painter(self):
        self.assertEqual(min_time_to_paint(1, 5, [10, 5, 7]), 110)

    def test_painter_time_one(self):
        self.assertEqual(min_time_to_paint(5, 1, [1, 2, 3, 4, 5]), 5)

    def test_many_painters(self):
        self.assertEqual(min_time_to_paint(100, 1, [1, 2, 3, 4, 5]), 5)


    def test_min_time_to_paint_with_three_painters(self):
        arr = [30] + [1] * 99
        expected_result = 43
        result = min_time_to_paint(3, 1, arr)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
