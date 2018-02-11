import re
from paint_Utils import PaintUtils
import copy


class Painter:
    def __init__(self):
        self._paint_utils = None
        self.input_command = []
        self._layout_matrix = []

    print('Welcome to the Painter')
    MAX_WIDTH = 5000
    MAX_HEIGHT = 5000
    SHAPE_FILL_CHAR = 'X'
    INVALID_INPUT = 'Invalid Input. Input must be in format:' \
                    '\n\"C width height\" \n\"L x1 y1 x2 y2 \"'' \
	'' \n\"R x1 y1 x2 y2 \" \n\"B x y color(*)\"' \
                    '\n Outer Width must be between ' + '1 and ' + str(MAX_WIDTH) + '' \
                                                                                    '\n Height Height must be between ' + '1 and ' + str(
        MAX_HEIGHT) + ''
    INPUT_REGEX_VALIDATORS = {
        'C': '^[cC]{1} [0-9]{1,4} [0-9]{1,4}$',
        'L': '^[lL]{1} [0-9]{1,4} [0-9]{1,4} [0-9]{1,4} [0-9]{1,4}$',
        'R': '^[rR]{1} [0-9]{1,4} [0-9]{1,4} [0-9]{1,4} [0-9]{1,4}$',
        'B': '^[bB]{1} [0-9]{1,4} [0-9]{1,4} .{1}$'
    }
    NO_SHAPE_MESSAGE = 'Please draw the layout before any shape'

    def execute_command(self, input_cmd):
        is_input_valid = self.validate_input(input_cmd)
        if is_input_valid:
            self.draw(self.input_command)

    def validate_input(self, cmd):
        c_regex = re.compile(self.INPUT_REGEX_VALIDATORS['C'])
        m_regex = re.compile(self.INPUT_REGEX_VALIDATORS['L'])
        r_regex = re.compile(self.INPUT_REGEX_VALIDATORS['R'])
        b_regex = re.compile(self.INPUT_REGEX_VALIDATORS['B'])
        if len(cmd) > 0 and type(cmd) is str:
            cmd = cmd.strip()
        if len(c_regex.findall(cmd)) > 0 or len(m_regex.findall(cmd)) > 0 or len(r_regex.findall(cmd)) > 0 or len(
                b_regex.findall(cmd)) > 0:
            self.input_command = self.reshape_input(cmd)
            are_dim_valid = self.validate_dimensions(self.input_command)
            if (are_dim_valid):
                return True
            else:
                print(self.INVALID_INPUT)
        else:
            print(self.INVALID_INPUT)

    def reshape_input(self, input_cmd):
        cmd_array = []
        if len(input_cmd) > 0:
            cmd_array = cmd.replace('\"', '').split(" ")
            cmd_array[0] = cmd_array[0].upper()
        return cmd_array

    def validate_dimensions(self, cmd):
        if cmd[0] == 'C':
            print(cmd[1])
            return int(cmd[1]) > 0 and int(cmd[1]) < self.MAX_WIDTH - 1 and int(cmd[2]) < self.MAX_HEIGHT - 1
        if cmd[0] == 'L' or cmd[0] == 'R':
            return int(cmd[1]) > 0 and int(cmd[1]) < self.MAX_WIDTH - 1 and int(cmd[3]) < self.MAX_WIDTH - 1 and int(
                cmd[2]) < self.MAX_HEIGHT - 1 and int(cmd[4]) < self.MAX_HEIGHT - 1
        if cmd[0] == 'B':
            return int(cmd[1]) > 0 and int(cmd[1]) < self.MAX_WIDTH - 1 and int(cmd[2]) < self.MAX_HEIGHT - 1

    def draw(self, cmd):
        shape = str(cmd[0])
        layout_matrix = []
        try:
            if shape == 'C':
                self._paint_utils = PaintUtils(int(cmd[1]), int(cmd[2]))
                layout_matrix = self._paint_utils.draw_layout(int(cmd[1]), int(cmd[2]))
                self._layout_matrix = copy.deepcopy(layout_matrix)
                self._paint_utils.render(self._layout_matrix)
            elif shape == 'L' or shape == 'R':
                if self._paint_utils is None:
                    print(self.NO_SHAPE_MESSAGE)
                    return
                layout_matrix = self._paint_utils.draw_rectangle(
                    int(cmd[1]),
                    int(cmd[2]),
                    int(cmd[3]),
                    int(cmd[4]),
                    self.SHAPE_FILL_CHAR
                )
                self._layout_matrix = copy.deepcopy(layout_matrix)
                self._paint_utils.render(self._layout_matrix)
            elif shape == 'B':
                if self._paint_utils is None:
                    print(self.NO_SHAPE_MESSAGE)
                    return
                layout_matrix = self._paint_utils.fill_color(int(cmd[1]), int(cmd[2]), cmd[3])
                self._layout_matrix = copy.deepcopy(layout_matrix)
                self._paint_utils.render(self._layout_matrix)
        except Exception as e:
            print(str(e))


if __name__ == "__main__":
    in_command_loop = True
    painter = Painter()
    while in_command_loop:
        cmd = input("Enter Command: ")
        if cmd == 'Q':
            break
        painter.execute_command(cmd)
