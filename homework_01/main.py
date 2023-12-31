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
    quads = []
    for num in nums:
        quads.append(num**2)
    return quads


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(num):
    if num <= 1:
        return False
    elif num == 2 or num == 5 or num == 3:
        return True
    # убираем больше половины вариантов, если число делится на 2 или 3 или 5. Таких чисел много, процесс ускоряется
    elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
        return False
    # остальное перебираем
    else:
        for div in range(2, num):
            if num % div == 0:
                return False
        return True


def filter_numbers(nums, desired_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if desired_type == ODD:
        return [i for i in nums if i % 2 == 1]
    elif desired_type == EVEN:
        return [i for i in nums if i % 2 == 0]
    elif desired_type == PRIME:
        return list(filter(is_prime, nums))
