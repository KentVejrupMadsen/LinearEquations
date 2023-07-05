from abc                        \
    import                      \
    ABC,                        \
    abstractmethod

from LinearEquations.vectors    \
    import                      \
    VectorAbstract,             \
    Vector2D


# Maps a given input vector (ie. x, y) to a given value (z)
class VectorFunction(
    ABC
):
    def __init__(
        self,
        input_vector: VectorAbstract = Vector2D(
            x=0.0,
            y=0.0
        )
    ):
        self.input_position: VectorAbstract = input_vector

    def __del__(self):
        del self.input_position

    @abstractmethod
    def calculate(self) -> float:
        raise NotImplemented

    def is_input_position_none(self) -> bool:
        return self.input_position is None

    def get_input_position(self) -> VectorAbstract:
        return self.input_position

    def set_input_position(
        self,
        value: VectorAbstract
    ) -> None:
        self.input_position = value

    def move_input_position(
        self,
        values: list
    ):
        self.get_input_position().assign_values(
            values
        )
