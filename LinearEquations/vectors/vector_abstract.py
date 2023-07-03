from abc                    \
    import                  \
    ABC,                    \
    abstractmethod

from math                   \
    import                  \
    pow,                    \
    sqrt

from HardenedSteel.objects  \
    import                  \
    CounterObject

from HardenedSteel.globals \
    import \
    get_integer_zero

integer_two: int = 2
zero: float = 0.0

brackets_begin: int = ord('(')
brackets_end: int = ord(')')
delimiter: int = ord(',')


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


def get_zero() -> float:
    global zero
    return zero


def power_of_two(
    value: float
) -> float:
    return pow(
        value,
        get_integer_two()
    )


class VectorAbstract(
    ABC
):
    def __init__(self):
        super().__init__()

    def __del__(self):
        pass

    def __dir__(self) -> list:
        result: list = []
        return result

    def value_is_zero(
        self,
        value: float
    ) -> bool:
        return value == get_zero()

    def calculate_magnitude(self) -> float:
        result: float = get_zero()

        for key in dir(self):
            value: float = self[key]

            if not self.value_is_zero(
                value
            ):
                result: float = result + power_of_two(value)

        result: float = sqrt(
            result
        )

        return result

    def __float__(self) -> float:
        return self.calculate_magnitude()

    def __getitem__(
        self,
        item: str
    ):
        return getattr(
            self,
            str(item).lower()
        )

    def __repr__(self) -> str:
        result_dictionary: dict = dict()

        for entry in dir(self):
            value = self[entry]
            result_dictionary[entry] = value

        result: str = str(
            result_dictionary
        )

        return result

    def __str__(self):
        result: str = ''

        size_of: int = len(self)
        counter: CounterObject = CounterObject(
            start_value=get_integer_zero()
        )

        while counter.get_value() < size_of:
            current_index: int = counter.get_value()

            entry = dir(self)[current_index]
            result = result + str(self[entry])

            next_position: int = counter.after()
            if next_position < size_of:
                result = result + get_delimiter() + ' '

            counter.increment()

        final_result: str = get_bracket_begins() + result + get_bracket_ends()
        return final_result

    def __len__(self) -> int:
        return len(
            dir(self)
        )
