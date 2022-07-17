
# ##############################################################################
# Imports
# ##############################################################################

# General.
import pathlib

# ##############################################################################
# Classes
# ##############################################################################


class TestMetaclass(type):
    def __new__(cls, clsname, bases, clsdict):
        print(clsdict)
        print(bases)
        print(clsname)
        return super().__new__(cls, clsname, bases, clsdict)

class TestClass(metaclass=TestMetaclass):
    def __init__(self):
        self.s = 0


# ##############################################################################
# Main Function
# ##############################################################################


def main() -> None:
    """
        Runs the main function.
    """
    test = TestClass()


# ##############################################################################
# Main Program
# ##############################################################################


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
