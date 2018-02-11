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

