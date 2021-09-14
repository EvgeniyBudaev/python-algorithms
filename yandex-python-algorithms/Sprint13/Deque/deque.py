# 53044384
class Deque:
    def __init__(self, n):
        self.__deque_list = [None] * n
        self.__max_size = n
        self.__front = self.__back = self.__size = 0

    def is_empty(self):
        """Проверить на пустоту."""
        return self.__size == 0

    def calc_index(self, var: int, val: int) -> int:
        if val:
            return (var + 1) % self.__max_size
        else:
            return (var - 1) % self.__max_size

    def overflow(self):
        """Проверить на переполнение."""
        return self.__size >= self.__max_size

    def push_back(self, value: int):
        """Добавить элемент в конец дека."""
        if self.overflow():
            raise OverfullError
        self.__deque_list[self.__back] = value
        self.__back = self.calc_index(self.__back, 1)
        self.__size += 1


    def push_front(self, value: int):
        """Добавить элемент в начало дека."""
        if self.overflow():
            raise OverfullError
        self.__deque_list[self.__front - 1] = value
        self.__front = self.calc_index(self.__front, 0)
        self.__size += 1

    def pop_front(self):
        """Вывести первый элемент дека и удалить его."""
        if self.is_empty():
            raise EmptyError
        front = self.__deque_list[self.__front]
        self.__deque_list[self.__front] = None
        self.__front = self.calc_index(self.__front, 1)
        self.__size -= 1
        return front

    def pop_back(self):
        """Вывести последний элемент дека и удалить его."""
        if self.is_empty():
            raise EmptyError
        back = self.__deque_list[self.__back - 1]
        self.__deque_list[self.__back - 1] = None
        self.__back = self.calc_index(self.__back, 0)
        self.__size -= 1
        return back


class EmptyError(Exception):
    """Выбрасывается исключение, когда двухсторонняя очередь пуста."""
    pass


class OverfullError(Exception):
    """Выбрасывается исключение, когда двухсторонняя очередь переполнена."""
    pass


def handle_commands(command, deque):
    """Команды."""
    function, *args = command.split()
    try:
        return getattr(deque, function)(*args)
    except AttributeError:
        raise ValueError('Invalid value')
    except (OverfullError, EmptyError):
        return 'error'


def main():
    number_commands = int(input())
    deque = Deque(int(input()))
    commands = [input() for _ in range(number_commands)]
    for command in commands:
        result = handle_commands(command, deque)
        if result:
            print(result)


if __name__ == '__main__':
    main()
