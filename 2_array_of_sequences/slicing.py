def slicing_examples() ->  None:
    lst = [42, -123, 10, 11]
    s = "damian is cool"

    print(f'lst: {lst}')
    print(f'first: {lst[:1]}')
    print(f'except first: {lst[1:]}')
    print(f'by step 2: {lst[::2]}')
    print(f'by step -1: {lst[::-1]}')
    print(f'reverse({s}) = {s[::-1]}')

    del lst[2:4]
    print(f'after del lst[2:4]: {lst}')


def ttt_board_example() -> None:
    board =[['_'] * 3 for _ in range(3)]
    print(board)
    board[1][2] = 'X'
    print(board)

    print('wrong board using * in initialization:')
    board_wrong = [['_'] * 3] * 3
    print(board_wrong)
    board_wrong[1][2] = 'X'
    print(board_wrong)


if __name__ == '__main__':
    slicing_examples()
    ttt_board_example()
