from typing import List
from collections import Counter

coefficient = '3'
coefficientTwo = int(coefficient) * 2
# row1 = '1999'
# row2 = '5436'
# row3 = '4368'
# row4 = '1712'

# row1 = '1111'
# row2 = '9999'
# row3 = '1111'
# row4 = '9911'

# row1 = '1111'
# row2 = '1111'
# row3 = '1111'
# row4 = '1111'

row1 = '1231'
row2 = '2..2'
row3 = '2..2'
row4 = '2..2'

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

print(list_all_symbols)

dict_symbols_count = dict(Counter(list_all_symbols))
print(dict_symbols_count)

new_dict = {key: value for key, value in dict_symbols_count.items() if coefficientTwo >= value and key != 0}
print(new_dict)
print(len(new_dict))
