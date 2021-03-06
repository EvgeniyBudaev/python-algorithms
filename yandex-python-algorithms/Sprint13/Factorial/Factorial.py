# Пример с рекурсией. Есть риски переполнения стека.
def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)


def factorial(n):
    accumulator = 1
    i = n
    while i > 1:
        accumulator *= i
        i -= 1
    return accumulator

# Объёмом памяти, который выделяется под стек вызовов, можно управлять.
# В некоторых языках это можно делать прямо в процессе работы программы.
# Например, в Python можно применить метод setrecursionlimit() модуля sys.
# Передаваемый в функцию параметр limit — задаёт максимальную глубину рекурсии.
# Наибольшее возможное значение зависит от платформы и всё равно существенно
# ограничено. Можно узнать текущее значение этой величины, вызвав метод
# getrecursionlimit().
# В других языках программирования, таких как Java и JavaScript, размер стека
# вызовов можно задать настройками виртуальной машины при запуске программы, но в
# процессе работы программы он остаётся неизменным.\\
# Кроме того, размер стека вызовов иногда может быть изменён на уровне
# операционной системы.