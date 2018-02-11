import unittest
from painter import Painter
from paint_Utils import Paint_Utils
import sys


class Test_Painter(unittest.TestCase):
    _width = 30
    _height = 30
    _max_width = 50
    _max_height = 50
    _paint_utils = Paint_Utils(_width, _height)

    def test_outer_generation(self):
        upper_char = '-'
        lower_char = '-'
        left_char = '|'
        right_char = '|'
        middle_char = '#'
        layout_matrix = self._paint_utils._Paint_Utils__outer_layout(self._width, self._height, upper_char, lower_char,
                                                                     left_char, right_char, middle_char)
        print('\nTesting if outer layout is built correctly')
        self.assertEqual(32, len(layout_matrix), 'Layout Size is correct')
        self.assertEqual('-', list(layout_matrix[0])[0], 'Layout borders are correct')
        self.assertEqual(32, len(list(layout_matrix[0])), 'Layout width is correct')

    def test_build_line(self):
        line = self._paint_utils._Paint_Utils__build_line(20, '*', '*', '*')
        print('\nTesting if the outer border is built correctly')
        self.assertEqual(22, len(line), 'Border size is correct')
        self.assertEqual(str, type(line), 'Border array type is correct')

    def test_build_line2(self):
        print('\nTesting if correct symbols are appended to line')
        line = self._paint_utils._Paint_Utils__build_line(20, '*', '*', ' ')
        self.assertEqual(22, len(line))
        self.assertEqual('*', list(line)[0])
        for i in range(1, len(line) - 1):
            self.assertEqual(' ', line[i])

    def test_update_line(self):
        print('\nTesting if the line is updated properly with symbols')
        prev_line = '------'
        line = self._paint_utils._Paint_Utils__update_line(prev_line, 2, 4, 'l', 'r', 'm')
        self.assertEqual('l', list(line)[2])
        self.assertEqual('r', list(line)[4])
        for i in range(3, 4):
            self.assertEqual('m', list(line)[i])

    def test_update_row_in_layout(self):
        print('\nTesting if rows are updated properly')
        _paint_utils = self._paint_utils
        _paint_utils._layout_matrix = ['a', 'b', 'c', 'd']
        _paint_utils._Paint_Utils__update_row_in_layout('z', 2)
        self.assertEqual('z', _paint_utils._layout_matrix[2])

    def test_get_line_from_layout(self):
        print('\nTesting if rows are retrieved properly')
        _paint_utils = self._paint_utils
        _paint_utils._layout_matrix = ['a', 'b', 'c', 'd']
        get_line = _paint_utils._Paint_Utils__get_line_from_layout(2)
        self.assertEqual('c', get_line)

    def test_draw_line(self):
        print("\nTesting if line is drawn properly with correct inputs")
        _paint_utils = self._paint_utils
        _paint_utils._layout_matrix = self._paint_utils._Paint_Utils__outer_layout(5, 5, '-', '-', '|', '|', ' ')
        _paint_utils.draw_rectangle(1, 1, 3, 1, 'L')
        self.assertEqual(7, len(_paint_utils._layout_matrix))
        for i in range(1, 4):
            self.assertEqual('L', list(_paint_utils._layout_matrix[1])[i])

    def test_draw_line_wrong_input(self):
        print('\nTesting if line is not drawn for wrong input. Message below')
        _paint_utils = self._paint_utils
        _paint_utils._layout_matrix = self._paint_utils._Paint_Utils__outer_layout(5, 5, '-', '-', '|', '|', ' ')
        _paint_utils.draw_rectangle(1, 10, 3, 3, 'L')
        row = '|     |'
        for i in range(1, 6):
            self.assertEqual(row, _paint_utils._layout_matrix[i], msg=None)

    def test_draw_rectangle(self):
        print("\nTesting if rectangle is drawn properly with correct inputs")
        _paint_utils = self._paint_utils
        _paint_utils._layout_matrix = self._paint_utils._Paint_Utils__outer_layout(5, 5, '-', '-', '|', '|', ' ')
        _paint_utils.draw_rectangle(1, 1, 3, 3, 'X')
        self.assertEqual(7, len(_paint_utils._layout_matrix))
        for i in range(1, 4):
            for j in (1, 3):
                self.assertEqual('X', list(_paint_utils._layout_matrix[i])[j])

    def test_draw_rect_wrong_input(self):
        print('\nTesting if line is not drawn for wrong input. Message below')
        _paint_utils = self._paint_utils
        _paint_utils._layout_matrix = self._paint_utils._Paint_Utils__outer_layout(5, 5, '-', '-', '|', '|', ' ')
        _paint_utils.draw_rectangle(1, 10, 3, 3, 'L')
        row = '|     |'
        for i in range(1, 6):
            self.assertEqual(row, _paint_utils._layout_matrix[i], msg=None)


if __name__ == '__main__':
    unittest.main()
