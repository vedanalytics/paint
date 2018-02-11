from utils import painter_utils
from utils import config
import sys
import os
import copy
sys.path.insert(1, os.path.join(sys.path[0], '..'))


class Rectangle:
    def __init__(self, layout):
        self._layout = layout
        self._layout_height = len(layout) if len(layout) > 0 else 0
        self._layout_width = len(self._layout[0]) if len(self._layout) > 0 else 0
        self._border_char = config.RECTANGLE['border']

    def draw_shape(self, x1, y1, x2, y2, char=None):
        """
        Draw Rectangle

        Draw Rectangle from given inputs and border char.
        Updates the layout matrix for given dimensions.
        Render() should be called after this method to print the output.

        Parameters
        ----------
        x1 : int
            x1 of Rectangle
        y1 : int
            x1 of Rectangle
        x2 : int
            y1 of Rectangle
        y2 : int
            y2 of Rectangle
        char : str
            char, which is border of Rectangle

        Returns
        -------
        Layout Matrix

        """
        char = char if len(char) > 0 else self._border_char
        outer_layout = copy.deepcopy(self._layout)
        is_input_valid = painter_utils.is_input_valid(outer_layout, x1, y1, x2, y2)
        if is_input_valid:
            x1, y1, x2, y2 = painter_utils.order_inputs(x1, y1, x2, y2)
            outer_layout = self.__draw_rectangle(outer_layout, x1, y1, x2, y2, char)
        else:
            print('')
        return outer_layout

    def __draw_rectangle(self, layout, x1, y1, x2, y2, char):
        for i in range(y1, y2 + 1):
            if i == y1 or i == y2:
                line = copy.deepcopy(layout[i])
                line = painter_utils.update_line(line, x1, x2, char, char, char)
                layout[i] = line
            else:
                line = copy.deepcopy(layout[i])
                line = painter_utils.update_line(line, x1, x2, char, char, ' ')
                layout[i] = line
        return layout
