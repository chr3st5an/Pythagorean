from typing import NoReturn


class Pythagorean(object):
    def __init__(self, odd_num: int) -> None:
        """Initializes a pythagorean object

        Args:
            odd_num (int): An odd number to create the
            pythagorean triads based on

        Rises:
            AssertionError: The given number is not odd
            AttributeError: Can't delete attribute

        Example:
            A pythagorean object can be printed to the
            screen which will show the pythagorean triads
            equation

            >>> a = Pythagorean(7)
            >>> print(a)

            A pythagorean object can be also converted to
            an integer number which value will be the
            result of the pythagorean triads

            >>> res = int(a)

            The triads of the equation can be retrieved by
            using the triads attribute

            >>> triads = a.triads
        """
        assert odd_num % 2 != 0, "Number is not odd"
        self.__odd_num = odd_num
        self.__num = odd_num ** 2 // 2
        self.__result = self.__num + 1

    @property
    def triads(self) -> tuple:
        """
        Returns:
            Tuple[int]: The triads of the equation
        """
        return self.__odd_num, self.__num, self.__result

    def __repr__(self) -> str:
        return f'{self.__odd_num}^2 + {self.__num}^2 = {self.__result}^2'

    def __int__(self) -> int:
        return self.__result ** 2

    def __eq__(self, other) -> bool:
        return int(self) == int(other)

    def __gt__(self, other) -> bool:
        return int(self) > int(other)

    def __delattr__(self, name: str) -> NoReturn:
        raise AttributeError("Can't delete attribute")

    def __contains__(self, num: int) -> bool:
        return num in self.triads

    def __getitem__(self, index: int) -> int:
        return self.triads[index]

    def show_equation(self) -> None:
        return print(self)
