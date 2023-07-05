from LinearEquations.vectors    \
    import                      \
    get_float_zero,             \
    Vector1D


class Vector2D(
    Vector1D
):
    def __init__(
        self,
        x: float = get_float_zero(),
        y: float = get_float_zero(),
        lock: bool = True
    ):
        super().__init__(
            x=x,
            lock=False
        )
        self.insert_attribute(
            'y'
        )
        self.y: float = y
        self.set_lock(
            lock
        )

    def __del__(
        self
    ):
        super().__del__()
        del self.y

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

    def subtracting_y(
        self,
        y: float
    ):
        self.set_y(
            self.get_y() - y
        )
        return self.get_y()

    def addition_to_y(
        self,
        y: float
    ):
        self.set_y(
            self.get_y() + y
        )

    def set_all_to_zero(
        self
    ):
        self.set_x_to_zero()
        self.set_y_to_zero()

    def set_y_to_zero(
        self
    ) -> None:
        self.set_y(
            super().get_zero()
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

    def get_y(
        self
    ) -> float:
        return self.y

    def set_y(
        self,
        value: float
    ) -> None:
        self.y: float = value

