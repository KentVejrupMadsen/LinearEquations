class Vector2D:
    def __init__(
        self,
        x: float = 0.0,
        y: float = 0.0
    ):
        self.x: float = x
        self.y: float = y

    def __del__(self):
        del             \
            self.x,     \
            self.y

    def get_x(self) -> float:
        return self.x

    def set_x(
        self,
        value: float
    ) -> None:
        self.x: float = value

    def get_y(self) -> float:
        return self.y

    def set_y(
        self,
        value: float
    ) -> None:
        self.y: float = value
