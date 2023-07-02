from vectors \
    import Vector3D


def main_entry():
    test_vector: Vector3D = Vector3D(
        x=1.25,
        y=4.2,
        z=5.2
    )

    print(
        str(
            test_vector
        )
    )

    print(
        repr(
            test_vector
        )
    )


