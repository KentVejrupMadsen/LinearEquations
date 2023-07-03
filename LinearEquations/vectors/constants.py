zero: float = 0.0

integer_two: int = 2

brackets_begin: int = ord('(')
brackets_end: int = ord(')')
delimiter: int = ord(',')


def get_float_zero() -> float:
    global zero
    return zero


def get_delimiter() -> chr:
    global delimiter
    return chr(delimiter)


def get_bracket_begins() -> chr:
    global brackets_begin
    return chr(brackets_begin)


def get_bracket_ends() -> chr:
    global brackets_end
    return chr(brackets_end)


def get_integer_two() -> int:
    global integer_two
    return integer_two



