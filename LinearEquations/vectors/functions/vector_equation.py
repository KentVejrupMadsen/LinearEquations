from LinearEquations.vectors            \
    import                              \
    VectorAbstract,                     \
    Vector2D

from LinearEquations.vectors.functions  \
    import                              \
    VectorFunction


class VectorEquation(
    VectorFunction
):
    def __init__(
            self,
            input_position: VectorAbstract = Vector2D(
                x=0.0,
                y=0.0
            )
    ):
        super().__init__(
            input_vector=input_position
        )

    def __del__(
        self
    ):
        super().__del__()

    def calculate(self) -> float:
        return 0.0
