from vector2d \
    import Vector2D


def main():
    v1 = Vector2D(
        x=0.4,
        y=4.5
    )

    v2 = Vector2D(
        x=4.4,
        y=38.2
    )

    v1 = v1 + v2

    print(v1)


if __name__ == '__main__':
    main()
