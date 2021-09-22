# 53350958

from typing import List


def binary_search(numbers: List[int], left: int, right: int, item: int):
    """Бинарный поиск."""
    if left > right:
        return -1

    mid = (left + right) // 2
    if numbers[mid] == item:
        return mid

    if numbers[left] <= numbers[mid]:
        if numbers[left] <= item <= numbers[mid]:
            return binary_search(numbers, left, mid - 1, item)
        return binary_search(numbers, mid + 1, right, item)

    if numbers[mid] <= item <= numbers[right]:
        return binary_search(numbers, mid + 1, right, item)
    return binary_search(numbers, left, mid - 1, item)


def broken_search(nums: List[int], target: int) -> int:
    """Поиск индекса элемента в не отсротированном списке."""
    return binary_search(nums, 0, len(nums) - 1, target)


if __name__ == '__main__':
    input()
    target = int(input())
    array = [int(number) for number in input().split(' ')]
    print(broken_search(array, target))
