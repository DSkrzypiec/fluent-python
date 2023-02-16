from typing import List

def cart_product() -> List:
    colors = ['black', 'white', 'blue']
    sizes = ['S', 'M', 'L']
    return [(col, size) for col in colors for size in sizes]

def unpack_and_print_tuple() -> None:
    city, year = ('Warsaw', 2023)
    print(f"{city} in {year}")

def unpack_star_and_print() -> None:
    first, second, *rest = range(5)
    print(f"{first}, {second}, {rest}")

def nested_unpack_and_print() -> None:
    city, year, (lat, long) = ('Warsaw', 2023, (52.43, 23.98))
    print(f"Fake place in {city} in year {year}: ({lat}, {long})")

def tuple_patter_matching_print() -> None:
    records = [('Warsaw', 2023), ('Berlin', 2020), ('NYC', 2022)]
    for rec in records:
        match rec:
            case (_, year) if year >= 2022:
                print(f"Got record with year >= 2022: {rec}")


if __name__ == '__main__':
    print(cart_product())
    unpack_and_print_tuple()
    unpack_star_and_print()
    nested_unpack_and_print()
    tuple_patter_matching_print()
