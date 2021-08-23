my_list = [1, 2, 3, 4, 5, 6, 7, 8]  # упорядоченный список


def binary_search(list, item):
    low = 0
    high = len(list) - 1  # 8

    while low <= high:  # Пока эта часть не сократится до одного элемента...
        mid = (low + high) // 2  # проверяем средний элемент
        guess = list[mid]
        if guess == item:  # Значение найдено
            print("Значение найдено")
            return mid
        if guess > item:  # Много
            print("Много")
            high = mid - 1
        else:  # Мало
            print("Мало")
            low = mid + 1
    return None  # Значение не существует


print(binary_search(my_list, 3))  # тестируем функцию
