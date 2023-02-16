import math


class Vector:
    """ Home-grown Vector for testing dunder methods """


    def __init__(self, x: int=0, y: int=0) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Vector({self.x!r}, {self.y!r})"

    def __abs__(self) -> float:
        return math.hypot(self.x, self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == '__main__':
    v1 = Vector(2, 5)
    v2 = Vector(42, -17)

    print(f"v1: {v1} v2: {v2}")
    print(f"v1 + v2 = {v1 + v2}")
    print(f"|v2| = {abs(v2)}")
    print(f"v1 * 14 = {v1 * 14}")

