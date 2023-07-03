from math                   \
    import pow

from vectors                \
    import get_integer_two


def power_of_two(
    value: float
) -> float:
    return pow(
        value,
        get_integer_two()
    )
