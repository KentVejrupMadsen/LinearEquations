from abc                    \
    import                  \
    ABC,                    \
    abstractmethod

from math                   \
    import                  \
    sqrt

from vectors                \
    import                  \
    get_float_zero,         \
    power_of_two,           \
    get_delimiter,          \
    get_bracket_begins,     \
    get_bracket_ends,       \
    get_integer_zero

from HardenedSteel.objects  \
    import                  \
    CounterObject


class VectorAbstract(
    ABC
):
    def __init__(self):
        super().__init__()
        self.attributes: list = list()
        self.lock: bool = False

    def __del__(self):
        del                     \
            self.attributes,    \
            self.lock

    def __dir__(self) -> list:
        return self.get_attributes()

    def get_zero(self) -> float:
        return get_float_zero()

    def insert_attribute(
        self,
        value: str
    ) -> None:
        if bool(self):
            raise AssertionError('blocked by lock')

        self.get_attributes().append(
            value
        )

    def get_lock(self) -> bool:
        return self.lock

    def set_lock(
        self,
        with_value: bool
    ) -> None:
        self.lock = with_value

    def get_attributes(
        self
    ) -> list:
        return self.attributes

    def set_attributes(
        self,
        new_list: list
    ) -> None:
        self.attributes = new_list

    def exist_attribute(
        self,
        key: str
    ) -> bool:
        entry_key: str = key.lower()

        for selected_key in self.get_attributes():
            if entry_key == selected_key:
                return True

        return False

    def value_is_zero(
        self,
        value: float
    ) -> bool:
        return value == get_float_zero()

    def calculate_magnitude(
        self
    ) -> float:
        result: float = get_float_zero()

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

    def __float__(
        self
    ) -> float:
        return self.calculate_magnitude()

    def __getitem__(
        self,
        key: str
    ):
        entry: str = str(key).lower()

        return getattr(
            self,
            entry
        )

    def __setitem__(
        self,
        key: str,
        value: float
    ) -> None:
        entry: str = str(key).lower()

        setattr(
            self,
            entry,
            value
        )

    def __missing__(
        self,
        key: str
    ):
        raise TypeError(
            'attribute not found'
        )

    def __repr__(
        self
    ) -> str:
        result_dictionary: dict = dict()

        for entry in dir(self):
            value = self[entry]
            result_dictionary[entry] = value

        result: str = str(
            result_dictionary
        )

        return result

    def __str__(
        self
    ):
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

    def __len__(
        self
    ) -> int:
        return len(
            dir(self)
        )

    def __bool__(self):
        return self.get_lock()
