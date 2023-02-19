from collections import ChainMap

def dicts_basics() -> None:
    d1 = { 'a': 10, 'b': 42, **{ 'z': 99 } }
    d2 = { 'x': -42, 'y': 17, 'z': 88 }
    print(f'd1: {d1}')
    print(f'd1 | d2: {d1 | d2}')

def dictionary_views() -> None:
    print("dictionary_views:")
    d = dict(a=10, b=30, c=50)
    values = d.values()
    print(values)
    print(list(values))
    try:
        reversed(values)
    except:
        print("cannot revers dict_values")

    #print(values[0])

def chain_dicts() -> None:
    d1 = { 'a': 10, 'b': 42, **{ 'z': 99 } }
    d2 = { 'x': -42, 'y': 17, 'z': 88 }
    chain = ChainMap(d1, d2)
    print(f'chain: {chain}')
    print(f'chain[b]: {chain["b"]}')
    print(f'chain[z]: {chain["z"]}')
    print(f'chain[y]: {chain["y"]}')

if __name__ == '__main__':
    dicts_basics()
    dictionary_views()
    chain_dicts()


