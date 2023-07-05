from LinearEquations.vectors \
    import Vector1D


def test_by_default() -> None:
    assert True


def test_creation() -> None:
    test_value: float = 5.0
    test_vector: Vector1D = Vector1D(
        x=test_value
    )

    assert test_vector.get_x() == test_value


def test_assign() -> None:
    test_insert: float = 8.5
    test_creation_value: float = 2.4

    test_vector: Vector1D = Vector1D(
        x=test_creation_value
    )
    test_vector.assign_values([test_insert])

    assert test_vector.get_x() == test_insert
