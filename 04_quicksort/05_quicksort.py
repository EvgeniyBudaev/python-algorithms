def quicksort(array):
  if len(array) < 2:
    # Базовый случай: массивы с 0 и 1 элементом уже "отсортированы"
    return array
  else:
    # Рекурсивный случай
    pivot = array[0]
    # Подмассив всех элементов меньше опорного
    less = [i for i in array[1:] if i <= pivot]  # [5, 2, 3] => [2, 3] => []
    # Подмассив всех элементов больше опорного
    greater = [i for i in array[1:] if i > pivot]  # [] => [] => [3]
    return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([10, 5, 2, 3]))
