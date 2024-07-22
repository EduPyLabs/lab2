import doctest
import math


def check_point_belonging(x: float, y: float) -> bool:
    """
    Finds if point is belonging to given area.

    :param x: float
    :param y: float
    :return: bool

    >>> check_point_belonging(0, 0)
    True

    >>> check_point_belonging(6, 5)
    True

    >>> check_point_belonging(7, 5)
    False

    >>> check_point_belonging(-5, -5)
    False

    >>> check_point_belonging(5, -5)
    False

    >>> check_point_belonging(-4, 5)
    False

    """

    point_in_2_3_quarters = (-3 <= x <= 0) and ((4 // 3) * x <= y <= math.sqrt(abs(x ** 2 - 9)))

    case1 = (0 <= x <= 4) and (math.sqrt(abs(x ** 2 - 16)) * (-1) <= y <= x // 3 + 3)
    case2 = (4 <= x <= 6) and (2.5 * x - 10 <= y <= x // 3 + 3)

    point_in_1_4_quarters = case1 or case2

    result = point_in_2_3_quarters or point_in_1_4_quarters

    print(bool(result))


x = float(input("Input x coordinate:"))
y = float(input("Input y coordinate:"))

check_point_belonging(x, y)

doctest.testmod()
