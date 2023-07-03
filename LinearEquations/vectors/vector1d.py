from vectors            \
    import              \
    get_float_zero,     \
    VectorAbstract


class Vector1D(
    VectorAbstract
):
    def __init__(
        self,
        x: float = get_float_zero(),
        lock: bool = True
    ):
        super().__init__()
        self.insert_attribute(
            'x'
        )
        self.x: float = x

        self.set_lock(
            lock
        )

    def __del__(self):
        super().__del__()
        del self.x

    def set_x_to_zero(self) -> None:
        self.set_x(
            self.get_zero()
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
