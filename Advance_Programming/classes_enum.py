# define enumerations using the Enum base class
from enum import Enum, unique, auto

@unique # rquired a uniqe values as well items
class Fruit(Enum):
    APPLE=1
    BANANA=2
    ORANGE=3
    TOMATO=4
    PEER=auto()
    PIT=auto()
    PIX=auto()


def main():
   
    # TODO: enums have human-readable values and types
    print(Fruit.APPLE)
    print(type(Fruit.APPLE))
    print(repr(Fruit.APPLE))
    # TODO: enums have name and value properties
    print(Fruit.APPLE.name, Fruit.APPLE.value)
    # TODO: print the auto-generated value
    print(Fruit.PEER.value, Fruit.PIT.value, Fruit.PIX.value)
    # TODO: enums are hashable - can be used as keys
    myFruits = {}
    myFruits[Fruit.BANANA] = "Come Mr. Tally-man"
    print(myFruits[Fruit.BANANA])
    print(myFruits)
if __name__ == "__main__":
    main()
