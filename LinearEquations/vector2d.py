class Vector2D:
    def __init__(
        self,
        x: float = 0.0,
        y: float = 0.0
    ):
        self.x: float = x
        self.y: float = y

    def __del__(
        self
    ):
        del             \
            self.x,     \
            self.y

    def __add__(
        self,
        other
    ):
        result: Vector2D = Vector2D(
            x=self.get_x(),
            y=self.get_y()
        )

        if isinstance(
            other,
            Vector2D
        ):
            addition: Vector2D = other

            result.addition_to_x(
                addition.get_x()
            )

            result.addition_to_y(
                addition.get_y()
            )

        return result

    def __sub__(
        self,
        other
    ):
        result_vector: Vector2D = Vector2D(
            x=self.get_x(),
            y=self.get_y()
        )

        if isinstance(
            other,
            Vector2D
        ):
            subtracting: Vector2D = other

            result_vector.subtracting_x(
                subtracting.get_x()
            )

            result_vector.subtracting_y(
                subtracting.get_y()
            )

        return result_vector

    def subtracting_x(
        self,
        x: float
    ):
        self.set_x(
            self.get_x() - x
        )
        return self.get_x()

    def subtracting_y(
        self,
        y: float
    ):
        self.set_y(
            self.get_y() - y
        )
        return self.get_y()

    def addition_to_x(
        self,
        x: float
    ):
        self.set_x(
            self.get_x() + x
        )

    def addition_to_y(
        self,
        y: float
    ):
        self.set_y(
            self.get_y() + y
        )

    def set_all_to_zero(self):
        self.set_both(
            0.0,
            0.0
        )

    def set_both(
        self,
        x: float,
        y: float
    ):
        self.set_x(
            x
        )
        self.set_y(
            y
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

    def get_y(
        self
    ) -> float:
        return self.y

    def set_y(
        self,
        value: float
    ) -> None:
        self.y: float = value

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

    def __dir__(self) -> list:
        return [
            'x',
            'y'
        ]

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
