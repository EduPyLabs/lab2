# Лабораторна робота 2
![ua](https://img.shields.io/badge/lang-ua-blue.svg)

## Завдання 1

На координатній площині задана фігура (див. малюнок).
Користувач вводить **дві координати точки** і програма має визначити, чи попадає ця точка у **фігуру**. 

*Використовувати оператори галуження не потрібно, лише логічні оператори.*

![](/figure.png)

```
import doctest


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
    # Ваш код реалізації функції


# Ваш код, який реалізує введення координт точки x,y з клавіатури

check_point_belonging(x, y)

doctest.testmod()
```

## Завдання 2

Програма запитує вік користувача і в залежності від його віку відповідає: 
* *"Я думав, що Вам вік+1 рік/роки/років"*
* *"Ви ще не народилися"* (якщо вік менше нуля)
* *"Стільки не живуть..."* (якщо вік більше 140 років)

**Основне завдання** — це правильно написати закінчення `рік/роки/років`.
```

import doctest


def age_chat(age: int) -> None:
    """
    The program asks the user's age and, depending on his age, answers: "I thought your age was +1
    year/years/years" or "You have not been born yet" (if the age is less than zero) or "So many do not live..."
    (if the age is more than 140 years).

    :param age: int

    >>> age_chat(5)
    Я думав, що Вам 6 років

    >>> age_chat(23)
    Я думав, що Вам 24 роки

    >>> age_chat(20)
    Я думав, що Вам 21 рік

    >>> age_chat(-10)
    Ви ще не народилися

    >>> age_chat(155)
    Стільки не живуть...
    """
    # Ваш код реалізації функції


# Ваш код, який реалізує введення запиту від користувача на введення його віку age з клавіатури

age_chat(age)

doctest.testmod()
```
