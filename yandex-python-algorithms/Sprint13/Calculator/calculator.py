# 53044376
from operator import add, floordiv, mul, sub
from typing import List

OPERATORS = {
        '+': add,
        '-': sub,
        '/': floordiv,
        '*': mul
        }


class Stack:
    """Структура данных стек."""
    def __init__(self):
        self.__items = []

    def push(self, item):
        """Добавляет элемент на вершину стека."""
        self.__items.append(item)

    def peek(self):
        """ Возвращает элемент с вершины стека, не удаляя его."""
        return self.__items[-1]

    def pop(self):
        """Возвращает элемент с вершины стека и удаляет его."""
        return self.__items.pop()


def calculator(stack, symbols_list: List[str]):
    """Калькулятор."""
    for symbol in symbols_list:
        if symbol not in OPERATORS:
            stack.push(int(symbol))
        else:
            num_a, num_b = stack.pop(), stack.pop()
            stack.push(OPERATORS[symbol](num_b, num_a))

    return stack.pop()


def main(values: List[str]):
    return calculator(Stack(), values)


if __name__ == '__main__':
    values_list = list(map(str, input().split()))
    print(main(values_list))
