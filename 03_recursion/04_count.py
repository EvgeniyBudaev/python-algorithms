def count(arr):
    if not arr:
        return 0
    return 1 + count(arr[1:])


print(count([8, 3, 6, 5]))  # 4
