"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*nums):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    num_list = []
    for num in nums:
        num_list.append(num ** 2)
    return num_list


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(a):
    if a > 1:
        for n in range(2, int(a / 2) + 1):
            if (a % n) == 0:
                return False
        else:
            return True
    else:
        return False


def is_odd(num):
    return num % 2


def is_even(num):
    return num % 2 == 0


def filter_numbers(nums, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter_type == ODD:
        return list(filter(is_odd, nums))
    elif filter_type == EVEN:
        return list(filter(is_even, nums))
    else:
        return list(filter(is_prime, nums))



