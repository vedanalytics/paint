from utils import painter_utils
import copy
from Modules.layout import Layout
from Modules.rectangle import Rectangle
from Modules.fill_color import FillColor
import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))


class PaintUtils:
    def __init__(self, width, height):
        self._layout_matrix = []

        self._width = width
        self._height = height

        self.OVERFLOW_MESSAGES = {
            "X": "(x1,x2) should be between 1 and " + str(self._width),
            "Y": "(y1,y2) should be between 1 and " + str(self._height),
            "X_ORDER": "x2 must be greater than x1 ",
            "Y_ORDER": "y2 must be greater than y1 ",
            "FILL_COLOR": "x should be between 1 and " + str(self._width) + "" \
                                                                            "\ny should be between 1 and " + str(
                self._height) + "",
        }
        self.SHAPES = {
            "line": "L",
            "rectangle": "R",
            "fill_color": "B"
        }

    is_input_overflown = False

    def draw_line(self, x1, y1, x2, y2, char):
        """
        Draw Line

        Draw Line for given inputs and border char.
        Updates the layout matrix for given dimensions.
        Render() should be called after this method to print the output.

        Parameters
        ----------
        x1 : int
            x1 of Line
        y1 : int
            x1 of Line
        x2 : int
            y1 of Line
        y2 : int
            y2 of Line
        char : str
            char, which is border of Line

        Returns
        -------
        Layout Matrix with Line added inside

        """
        self.is_input_overflown = self.__verify_overflow(self._width, self._height, x1, y1, x2, y2)
        if not self.is_input_overflown:
            if y1 == y2 and x1 != x2:
                # Horizintal Line
                line = self.__get_line_from_layout(y1)
                line = self.__update_line(line, x1, x2, char, char, char)
                self.__update_row_in_layout(line, y1)
            if x1 == x2 and y1 != y2:
                # Vertical Line
                for i in range(y1, y2):
                    line = self.__get_line_from_layout(i)
                    line = self.__update_line(line, x1, x2, char, char, char)
                    self.__update_row_in_layout(line, i)

    def draw_rectangle(self, x1, y1, x2, y2, char):
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
        Layout Matrix with Rectangle added inside

        """
        layout = copy.deepcopy(self._layout_matrix)
        rectangle = Rectangle(layout)
        layout_matrix = rectangle.draw_shape(x1, y1, x2, y2, char)
        self._layout_matrix = layout_matrix
        return layout_matrix

    def fill_color(self, x, y, color):
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
        layout = copy.deepcopy(self._layout_matrix)
        fill_color = FillColor(layout)
        layout_matrix = fill_color.draw_shape(x, y, color)
        self._layout_matrix = copy.deepcopy(layout_matrix)
        return layout_matrix

    def draw_layout(self, width, height):
        """
        Draw Layout

        Draws layout using width and height
        Updates the layout matrix for given dimensions.
        Render() should be called after this method to print the output.

        Parameters
        ----------
        width:
        height:

        Returns
        -------
        Layout Matrix

        """
        layout = Layout(width, height)
        layout_matrix = layout.draw_shape()
        self._layout_matrix = layout_matrix
        return layout_matrix

    def render(self, layout):
        if not self.is_input_overflown:
            for item in layout:
                print(''.join(item))
