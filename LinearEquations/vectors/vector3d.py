from vectors \
    import Vector2D

zero: float = 0.0


def get_zero() -> float:
    global zero
    return zero


class Vector3D(
    Vector2D
):
    def __init__(
        self,
        x: float = get_zero(),
        y: float = get_zero(),
        z: float = get_zero()
    ):
        super().__init__(
            x,
            y
        )
        self.insert_attribute(
            'z'
        )
        self.z: float = z

    def __del__(self):
        super().__del__()
        del self.z

    def get_z(self) -> float:
        return self.z

    def set_z(
        self,
        value: float
    ) -> None:
        self.z = value

    def addition_to_z(
        self,
        value: float
    ) -> None:
        self.set_z(
            self.get_z()
            +
            value
        )

    def subtracting_z(
        self,
        value: float
    ) -> None:
        self.set_z(
            self.get_z()
            -
            value
        )

