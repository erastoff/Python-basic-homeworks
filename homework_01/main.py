"""
Домашнее задание №1
Функции и структуры данных
"""

def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [item ** 2 for item in args]

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(n):
    i = 2
    if n < 2:
        return False
    while i*i <= n:
        if n % i == 0:
            i += 1
            return False
        else:
            i += 1
            continue
    return True

def filter_numbers(nums, fltr):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if fltr == ODD:
        return list(filter(lambda x: x % 2 != 0, nums))
    elif fltr == EVEN:
        return list(filter(lambda x: x % 2 == 0, nums))
    elif fltr == PRIME:
        return list(filter(is_prime, nums))
    else:
        print('Unexpected filter!')
        return None