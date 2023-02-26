def intro_encoding_decoding() -> None:
    yellow = 'żółty'
    print(f'len(żółty) = {len(yellow)}')
    encoded = yellow.encode("utf8")
    print(f'encoded UTF-8: {encoded} with len: {len(encoded)}')
    print(f'decoded encoded: {encoded.decode("utf8")}')

def bytes_examples() -> None:
    yellow_b = bytes('żółty', encoding='utf_8')
    print(f'yello bytes: {yellow_b}')
    print(f'First byte: {yellow_b[0]}')
    print(f'First 3 bytes: {yellow_b[0:3]}')

if __name__ == '__main__':
    intro_encoding_decoding()
    bytes_examples()

