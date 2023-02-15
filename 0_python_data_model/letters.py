class Letters:
    def __init__(self):
        self._letters = "abcdefghijklmnop"

    def __len__(self) -> int:
        return len(self._letters)

    def __getitem__(self, position) -> str:
        return self._letters[position]

    def __repr__(self) -> str:
        return f"Letters({self._letters})"


if __name__ == '__main__':
    l = Letters()

    # Just by implementing __len__ and __getitem__ we got the following!
    print(len(l))
    print(l[0])
    print(l[0:5])

    for char in l:
        print(char)

    if "d" in l:
        print("d in letters!")

    print(l)
