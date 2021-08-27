# ID: 52461334

from typing import List
from collections import Counter


def replace_dots_to_zero(word: str) -> str:
    """Заменяет в строке символы . на 0"""
    return word.replace('.', '0')


def counter_scores(all_values: List[int], factor: int) -> int:
    """Подсчет максимального кол-ва баллов."""
    new_dict = {
        key: value
        for key, value in Counter(all_values).items()
        if (factor * 2) >= value and key != 0
    }

    return len(new_dict)


def main(all_values: List[int], factor: int) -> int:
    """Бизнес-логика при запуске этого модуля как основного!"""
    return counter_scores(all_values, factor)


if __name__ == '__main__':
    all_numbers: List[int] = []
    coefficient = int(input())
    for row in range(4):
        all_numbers.extend(list(map(int, replace_dots_to_zero(input()))))
    result = main(all_numbers, coefficient)
    print(result)
