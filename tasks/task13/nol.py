# ID: 52411374

from typing import List

street_length = input()
house_numbers = input()
listNumbers = list(map(int, house_numbers.split()))


def nearest_zero(distance: List[int]):
    zeros = [float('inf')] * len(distance)
    index_zeros = [i for i in range(len(distance)) if distance[i] == 0]
    for i in range(index_zeros[0], len(distance), +1):
        if distance[i] == 0:
            zeros[i] = 0
        else:
            zeros[i] = zeros[i-1] + 1
    for i in range(index_zeros[-1], index_zeros[0], -1):
        if distance[i] == 0:
            zeros[i] = 0
        else:
            zeros[i] = min(zeros[i], zeros[i + 1] + 1)
    for i in range(index_zeros[0] - 1, -1, -1):
        zeros[i] = zeros[i + 1] + 1
    result = ' '.join(str(x) for x in zeros)
    return result


print(nearest_zero(listNumbers))