from vector2d       \
    import Vector2D


def main():
    point_a: Vector2D = Vector2D(
        x=4.0,
        y=4.0
    )

    point_b: Vector2D = Vector2D(
        x=8.0,
        y=8.0
    )

    result: Vector2D = point_b - point_a

    print(repr(result))





if __name__ == '__main__':
    main()
