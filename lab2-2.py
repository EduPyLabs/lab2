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
    age_add_one = age + 1
    if age < 0:
        print("Ви ще не народилися")
    elif age > 140:
        print("Стільки не живуть...")
    elif age_add_one % 10 == 1 and age_add_one % 100 != 11:
        print(f"Я думав, що Вам {age_add_one} рік")
    elif 2 <= age_add_one % 10 <= 4:
        print(f"Я думав, що Вам {age_add_one} роки")
    else:
        print(f"Я думав, що Вам {age_add_one} років")


age = int(input("Введіть Ваш вік:"))

age_chat(age)

doctest.testmod()
