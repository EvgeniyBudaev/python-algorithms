# ID: 52411713

from typing import List
from collections import Counter

coefficient = int(input())
coefficientTwo = coefficient * 2
row1 = input()
row2 = input()
row3 = input()
row4 = input()

list_all_symbols = []


def change_word(word):
    for letter in word:
        if letter == ".":
            word = word.replace(letter, "0")
    return word


def get_list_all_symbols(list_numbers: List[int]):
    list_all_symbols.extend(list_numbers)


row_transform1 = change_word(row1)
row_transform2 = change_word(row2)
row_transform3 = change_word(row3)
row_transform4 = change_word(row4)

get_list_all_symbols(list(map(int, row_transform1)))
get_list_all_symbols(list(map(int, row_transform2)))
get_list_all_symbols(list(map(int, row_transform3)))
get_list_all_symbols(list(map(int, row_transform4)))

dict_symbols_count = dict(Counter(list_all_symbols))

new_dict = {key: value for key, value in dict_symbols_count.items() if coefficientTwo >= value and key != 0}

print(len(new_dict))