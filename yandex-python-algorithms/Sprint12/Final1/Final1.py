# from typing import List
# house_numbers = '0 1 4 9 0'
# # street_length = input()
# # house_numbers = input()
# listNumbers = list(map(int, house_numbers.split()))
#
#
# def nearest_zero(distance: List[int]):  # [0, 1, 4, 9, 0]
#     value_near = 0
#     zeros = [float('inf')] * len(distance)  # [inf, inf, inf, inf, inf]
#     index_zeros = [i for i in range(len(distance)) if distance[i] == value_near]  # [0, 4]
#
#     for i in range(index_zeros[0], len(distance)):
#         if distance[i] == value_near:
#             zeros[i] = 0
#         else:
#             zeros[i] = zeros[i-1] + 1
#     for i in range(index_zeros[-1], index_zeros[0], -1):
#         if distance[i] == value_near:
#             zeros[i] = 0
#         else:
#             zeros[i] = min(zeros[i], zeros[i + 1] + 1)
#     for i in range(index_zeros[0] - 1, -1, -1):
#         zeros[i] = zeros[i + 1] + 1
#     result = ' '.join(str(x) for x in zeros)
#     return result
#
#
# print(nearest_zero(listNumbers))


# Вариант 2
# house_numbers = list(map(int, input().split()))
#
# for i in range(len(house_numbers)):
#     if house_numbers[i] != 0:
#         b = [list(reversed(house_numbers[:i + 1])), house_numbers[i:]]
#         left = b[0].index(0) if 0 in b[0] else len(house_numbers)
#         right = b[1].index(0) if 0 in b[1] else len(house_numbers)
#         house_numbers[i] = min(left, right)
# result = ' '.join(str(x) for x in house_numbers)
# print(result)


def zero_dists(start, seq):
    """Дистанция до 0"""
    value = '0'
    d = start
    for n in seq:
        if n == value:
            d = 0
        else:
            d += 1
        yield d


# input()
numbers = input().split()

to_left = zero_dists(len(numbers), numbers)
to_right = reversed(tuple(zero_dists(len(numbers), reversed(numbers))))

print(*map(min, zip(to_left, to_right)))
