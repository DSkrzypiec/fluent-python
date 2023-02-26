from collections import namedtuple
from dataclasses import dataclass
from typing import NamedTuple, get_type_hints

class CoordinateClass:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

CoordinateNT = namedtuple('CoordinateNT', 'lat lon')

CoordinateNTT = NamedTuple('CoordinateNTT', lat=float, lon=float)

@dataclass(frozen=True)
class CooridinateDC:
    lat: float
    lon: float

    def __str__(self) -> str:
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}{ns}, {abs(self.lon):.1f}{we}'


def class_example() -> None:
    print('--- class example ---')
    moscow = CoordinateClass(55.76, 37.62)
    print(moscow)
    location = CoordinateClass(55.76, 37.62)
    print(location)
    print(f'location == moscow: {location == moscow}')

def namedtuple_example() -> None:
    print('--- namedtuple example ---')
    print(f'issubclass(CoordinateNT, tuple): {issubclass(CoordinateNT, tuple)}')
    moscow = CoordinateNT(55.756, 37.617)
    print(moscow)
    location = CoordinateNT(55.756, 37.617)
    print(f'location == moscow: {location == moscow}')

def namedtupletyping_example() -> None:
    print('--- typing.NameTuple example ---')
    moscow = CoordinateNTT(lat=55.756, lon=37.617)
    print(moscow)
    print(f'issubclass(CoordinateNTT, tuple): {issubclass(CoordinateNTT, tuple)}')
    print(f'type hints: {get_type_hints(CoordinateNTT)}')
    print(f'location == moscow: {CoordinateNTT(lat=55.756, lon=37.617) == moscow}')

def dataclass_example() -> None:
    print('--- dataclass example ---')
    moscow = CooridinateDC(55.756, 37.617)
    print(moscow)
    print(f'type hints: {moscow.__annotations__}')
    print(f'location == moscow: {CooridinateDC(55.756, 37.617) == moscow}')
    #print(f'Moving Moscow to south:')
    # moscow.lat = 40.00 # that raises FrozenInstanceError

if __name__ == '__main__':
    class_example()
    namedtuple_example()
    namedtupletyping_example()
    dataclass_example()
