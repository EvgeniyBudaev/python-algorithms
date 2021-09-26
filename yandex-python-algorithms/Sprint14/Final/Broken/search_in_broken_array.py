# 53516660

from typing import List


def broken_search(numbers: List[int], target: int) -> int:
    """Функция возвращает индекс элемента, равного item, если такой есть в
    массиве. Если элемент не найден, функция возвращает -1 """
    left, right = 0, len(numbers) - 1
    if left > right:
        return -1

    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == target:
            return mid
        if numbers[mid] <= numbers[right]:
            if numbers[mid] < target <= numbers[right]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if numbers[left] <= target < numbers[mid]:
                right = mid - 1
            else:
                left = mid + 1
    return -1


if __name__ == '__main__':
    """В первой строке вводится число n –— длина массива.
    Во второй строке вводится положительное число k –— искомый элемент.
    Далее в строку через пробел вводится n натуральных чисел."""
    input()
    k = int(input())
    array = [int(number) for number in input().split(' ')]
    print(broken_search(array, k))
