from vectors                \
    import                  \
    get_float_zero,         \
    Vector2D


class Vector3D(
    Vector2D
):
    def __init__(
        self,
        x: float = get_float_zero(),
        y: float = get_float_zero(),
        z: float = get_float_zero()
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

    def set_z_to_zero(self) -> None:
        self.set_z(
            self.get_zero()
        )

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

