import copy
from utils import validations
import os
import sys
import copy
sys.path.insert(1, os.path.join(sys.path[0], '..'))

OVERFLOW_MESSAGES = {
            "X": "(x1,x2) should be between 1 and ",
            "Y": "(y1,y2) should be between 1 and ",
            "X_ORDER": "x2 must be greater than x1 ",
            "Y_ORDER": "y2 must be greater than y1 ",
            "FILL_COLOR": "x should be between 1 and "  + "" \
                                                                            "\ny should be between 1 and " + "",
        }


def update_line(line_arr, x1, x2, left_char, right_char, middle_char):
    if len(line_arr) > 0 and 0 < x1 < len(line_arr) and 0 < x2 < len(line_arr):
        for i in range(x1, x2 + 1):
            if i == x1:
                line_arr[i] = left_char
            elif x1 < i < x2:
                if len(middle_char.strip()) > 0:
                    line_arr[i] = middle_char
            elif i == x2:
                line_arr[i] = right_char
    return line_arr


def __update_row_in_layout(row, idx):
    _layout_matrix[idx] = row


def __get_line_from_layout(self, row_idx):
    # Creating a copy of the matrix in order to avoid binding. If assigned directly, only reference gets copied
    row = copy.deepcopy(self._layout_matrix)
    return row[row_idx]


def __verify_fill_color_overflow(width, height, x, y):
    if x < 1 or x > width or y < 1 or y > height:
        return True
    return False


def order_inputs(x1, y1, x2, y2):
    if x1 > x2:
        x1, x2 = swap_inputs(x1,x2)
    if y1 > y2:
        y1, y2 = swap_inputs(y1,y2)
    return x1, y1, x2, y2


def swap_inputs(a,b):
    return b, a


def is_input_valid(layout, x1, y1, x2, y2):
    width = len(layout)
    height = len(layout[0]) if width > 0 else 0
    if x1 < 1 or x1 > width or x2 < 1 or x2 > width:
        return False
    if y1 < 1 or y1 > height or y2 < 1 or y2 > height:
        return False
    return True
