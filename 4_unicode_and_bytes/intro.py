def intro_encoding_decoding() -> None:
    yellow = 'żółty'
    print(f'len(żółty) = {len(yellow)}')
    encoded = yellow.encode("utf8")
    print(f'encoded UTF-8: {encoded} with len: {len(encoded)}')
    print(f'decoded encoded: {encoded.decode("utf8")}')


if __name__ == '__main__':
    intro_encoding_decoding()
