from utils import painter_utils
from utils import config
import sys
import os
import copy
sys.path.insert(1, os.path.join(sys.path[0], '..'))


class Layout:
    def __init__(self, width, height):
        self._config = config.OUTER_LAYOUT
        self._width = width
        self._height = height

    def draw_shape(self):
        """
        Draw Layout

        Draws layout using width and height
        Updates the layout matrix for given dimensions.
        Render() should be called after this method to print the output.

        Parameters
        ----------
        None

        Returns
        -------
        Layout Matrix

        """
        upper_char = self._config["upper_char"]
        lower_char = self._config["lower_char"]
        left_char = self._config["left_char"]
        right_char = self._config["right_char"]
        middle_char = self._config["middle_char"]
        layout = self.__draw_outer_layout(
            self._width,
            self._height,
            upper_char,
            lower_char,
            left_char,
            right_char,
            middle_char
        )
        return layout

    def __draw_outer_layout(self, width, height, upper_char, lower_char, left_char, right_char, middle_char):
        upper_edge_line = self.__build_line(width, upper_char, upper_char, upper_char)
        lower_edge_line = self.__build_line(width, lower_char, lower_char, lower_char)
        middle_line = self.__build_line(width, left_char, right_char, middle_char)
        layout = []
        for i in range(0, height + 2):
            if i == 0:
                layout.append(copy.deepcopy(upper_edge_line))
            elif 0 < i < height + 1:
                layout.append(copy.deepcopy(middle_line))
            elif i == height + 1:
                layout.append(copy.deepcopy(lower_edge_line))
        return layout

    def __build_line(self, width, left_char, right_char, middle_char):
        line = []
        for i in range(0, width + 2):
            if i == 0:
                line.append(left_char)
            elif 0 < i < width + 1:
                line.append(middle_char)
            elif i == width + 1:
                line.append(right_char)
        return line



