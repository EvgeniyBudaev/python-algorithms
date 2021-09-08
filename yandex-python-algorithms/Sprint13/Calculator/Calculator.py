# 52750974
import operator


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Добавляет элемент на вершину стека."""
        self.items.append(item)

    def peek(self):
        """ Возвращает элемент с вершины стека, не удаляя его."""
        return self.items[-1]

    def pop(self):
        """Возвращает элемент с вершины стека и удаляет его."""
        return self.items.pop()


def division(first, second):
    """Деление."""
    if second != 0:
        return first // second


def operator_choose(symbol, first, second):
    """Выбор оператора."""
    return {'+': operator.add(first, second),
            '-': operator.sub(first, second),
            '*': operator.mul(first, second),
            '/': division(first, second),
            }.get(symbol)


def calculator(expression):
    """Калькулятор."""
    expression = list(expression)
    for commands in expression:
        if (commands != '+' and commands != '-' and commands != '/'
                and commands != '*'):
            stack.push(int(commands))
        else:
            second_operand = int(stack.pop())
            first_operand = int(stack.peek())
            symbol = commands
            stack.items[-1] = operator_choose(symbol,
                                              first_operand,
                                              second_operand)
    return stack.peek()


if __name__ == '__main__':
    stack = Stack()
    print(calculator(input().split()))
