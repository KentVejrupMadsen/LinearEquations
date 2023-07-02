zero: float = 0.0


def get_zero() -> float:
    global zero
    return zero


class Vector1D:
    def __init__(
        self,
        x: float
    ):
        self.x: float = x

    def __del__(self):
        del self.x

    def set_x_to_zero(self) -> None:
        self.set_x(
            get_zero()
        )

    def get_x(
        self
    ) -> float:
        return self.x

    def set_x(
        self,
        value: float
    ) -> None:
        self.x: float = value

    def addition_to_x(
        self,
        x: float
    ):
        self.set_x(
            self.get_x() + x
        )

    def subtracting_x(
        self,
        x: float
    ):
        self.set_x(
            self.get_x() - x
        )
        return self.get_x()

    def __dir__(self) -> list:
        result: list = ['x']
        return result

    def __len__(self) -> int:
        return len(
            dir(self)
        )

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

        end: int = len(self)

        for i in range(end):
            entry = dir(self)[i]
            result = result + str(self[entry])

            actual_position: int = i + 1
            if actual_position < end:
                result = result + ', '

        final_result: str = '(' + result + ')'
        return final_result
