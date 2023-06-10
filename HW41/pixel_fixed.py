from __future__ import annotations
import random


class Pixel:

    def __init__(self, r, g, b):
        if len(list(filter(lambda component: 0 <= component <= 255, [r, g, b]))) != 3:
            raise ValueError(f"One of the Pixel components ({r}, {g}, {b}) is not in range of [0, 255]")
        self.__r = int(r)
        self.__g = int(g)
        self.__b = int(b)

    @property
    def r(self):
        return self.__r

    @property
    def g(self):
        return self.__g

    @property
    def b(self):
        return self.__b

    def __add__(self, other: Pixel):
        new_r = Pixel._convert_to_byte(self.__r + other.__r)
        new_g = Pixel._convert_to_byte(self.__g + other.__g)
        new_b = Pixel._convert_to_byte(self.__b + other.__b)
        return Pixel(new_r, new_g, new_b)

    def __sub__(self, other: Pixel):
        new_r = Pixel._convert_to_byte(self.__r - other.__r)
        new_g = Pixel._convert_to_byte(self.__g - other.__g)
        new_b = Pixel._convert_to_byte(self.__b - other.__b)
        return Pixel(new_r, new_g, new_b)

    def __pixel_multiplication(self, multiplicator):
        Pixel._check_if_value_is_int_or_float(multiplicator)
        Pixel._check_if_value_greater_than_zero(multiplicator)
        new_r = Pixel._convert_to_byte(self.__r * multiplicator)
        new_g = Pixel._convert_to_byte(self.__g * multiplicator)
        new_b = Pixel._convert_to_byte(self.__b * multiplicator)
        return Pixel(new_r, new_g, new_b)

    def __mul__(self, multiplicator):
        return self.__pixel_multiplication(multiplicator)

    def __rmul__(self, multiplicator):
        return self.__pixel_multiplication(multiplicator)

    def __truediv__(self, multiplicator):
        Pixel._check_if_value_is_int_or_float(multiplicator)
        Pixel._check_if_value_greater_than_zero(multiplicator)
        new_r = Pixel._convert_to_byte(int(self.__r / multiplicator))
        new_g = Pixel._convert_to_byte(int(self.__g / multiplicator))
        new_b = Pixel._convert_to_byte(int(self.__b / multiplicator))
        return Pixel(new_r, new_g, new_b)

    def __eq__(self, other: Pixel):
        return self.__r == other.__r and self.__g == other.__g and self.__b == other.__b

    def __str__(self):
        return f"Pixel object\n\tRed: {self.__r}\n\tGreen: {self.__g}\n\tBlue: {self.__b}\n"

    def __repr__(self):
        return f"Pixel({self.__r}, {self.__g}, {self.__b})"

    def get_pixel_near(self, area):
        neighbourhood = int(-area + 2 * area * random.random())
        r_ = abs(self.r + neighbourhood)
        g_ = abs(self.g + neighbourhood)
        b_ = abs(self.b + neighbourhood)
        if all(0 <= c <= 255 for c in [r_, g_, b_]):
            return Pixel(r_, g_, b_)
        else:
            return self.get_pixel_near(area)

    @staticmethod
    def _check_if_value_is_int_or_float(n):
        if not isinstance(n, (int, float)):
            raise TypeError("Pixel could be multiplied only by int or float")

    @staticmethod
    def _check_if_value_greater_than_zero(n):
        if n <= 0:
            raise ValueError("Multiplicator should be greater than 0")

    @staticmethod
    def _convert_to_byte(n: int):
        if n < 0:
            return 0
        elif n > 255:
            return 255
        else:
            return n
