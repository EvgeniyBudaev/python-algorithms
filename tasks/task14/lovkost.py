# ID: 52424425

from typing import List
from collections import Counter


def replace_dots_to_zero(word):
    """Заменяет в строке символы . на 0"""
    return word.replace('.', '0')


def main():
    """Бизнес-логика при запуске этого модуля как основного!"""
    all_numbers: List[int] = []
    coefficient = int(input())

    for row in range(4):
        all_numbers.extend(list(map(int, replace_dots_to_zero(input()))))

    new_dict = {
        key: value
        for key, value in Counter(all_numbers).items()
        if (coefficient * 2) >= value and key != 0
    }

    print(len(new_dict))


if __name__ == '__main__':
    main()
