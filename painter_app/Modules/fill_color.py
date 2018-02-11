from utils import painter_utils
from utils import config
import sys
import os
import copy
sys.path.insert(1, os.path.join(sys.path[0], '..'))


class FillColor:
    def __init__(self, layout):
        self._layout = layout

    def draw_shape(self, x, y, color):
        """
        Fill Area with given color

        Fills the area around given space using given color.
        Updates the layout matrix for given dimensions.
        Render() should be called after this method to print the output.

        Parameters
        ----------
        x : int
            x in space
        y : int
            y in space
        color : str
            color to fill space
        Returns
        -------
        Layout matrix filled with color from x,y

        """
        outer_layout = copy.deepcopy(self._layout)
        width, height = len(outer_layout[0]), len(outer_layout)
        to_replace = ' '
        to_fill = set()
        to_fill.add((x, y))
        while to_fill:
            x, y = to_fill.pop()
            if not (1 <= x < width and 1 <= y < height):
                continue
            value = outer_layout[x][y]
            if value != to_replace:
                continue
            outer_layout[x][y] = color
            to_fill.add((x - 1, y))
            to_fill.add((x + 1, y))
            to_fill.add((x, y - 1))
            to_fill.add((x, y + 1))
        return outer_layout
