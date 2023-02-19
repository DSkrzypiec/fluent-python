class P:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'P({self.x}, {self.y})'


def set_operations() -> None:
    p1 = P(42, 13)
    p2 = P(-1, 1)
    p3 = P(100, 99)

    s1 = { p1, p2 }
    s2 = { p2, p3 }

    print(f's1: {s1}')
    print(f's2: {s2}')
    print(f'p1.__hash__() = {p1.__hash__()}')

    print(f'Sum s1 | s2: {s1 | s2}')
    print(f'Diff s1 - s2: {s1 - s2}')
    print(f'Inters s1 & s2: {s1 & s2}')


def set_operators() -> None:
    print('set operators:')
    s1 = { 1, 2, 8, 10 }
    print(f's1: {s1}')

    print(f'2 in s1: {2 in s1}')
    sub1 = {2, 8}
    print(f'(2, 8) is subset of s1: {sub1 < s1}')
    print(f's1 <= s1: {s1 <= s1}')

    s1.add(13)
    s1.add(13)
    print(f'after added 13 twice, s1: {s1}')


if __name__ == '__main__':
    set_operations()
    set_operators()
