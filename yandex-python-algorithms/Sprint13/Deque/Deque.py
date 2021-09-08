# 52750674
class Deque:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_size = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        """Проверить на пустоту."""
        return self.size == 0

    def overflow(self):
        """Проверить на переполнение."""
        return self.size >= self.max_size

    def push_back(self, item):
        """Добавить элемент в конец дека."""
        if self.overflow():
            raise OverfullError
        self.queue[self.tail] = item
        self.tail = (self.tail + 1) % self.max_size
        self.size += 1

    def push_front(self, item):
        """Добавить элемент в начало дека."""
        if self.overflow():
            raise OverfullError
        if self.head == 0 and self.tail == 0:
            self.queue[self.head] = item
            self.tail = (self.tail + 1) % self.max_size
        elif self.head == 0 and self.tail == 1:
            self.head = self.max_size - 1
            self.queue[self.head] = item
        else:
            self.head = (self.head - 1) % self.max_size
            self.queue[self.head] = item
        self.size += 1

    def pop_front(self):
        """Вывести первый элемент дека и удалить его."""
        if self.is_empty():
            raise EmptyError
        item = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return item

    def pop_back(self):
        """Вывести последний элемент дека и удалить его."""
        if self.is_empty():
            raise EmptyError
        if self.tail == 0:
            self.tail = self.max_size - 1
            item = self.queue[self.tail]
            self.queue[self.tail] = None
        else:
            self.tail = (self.tail - 1) % self.max_size
            item = self.queue[self.tail]
            self.queue[self.tail] = None
        self.size -= 1
        return item


class EmptyError(Exception):
    """Выбрасывается исключение, когда двухсторонняя очередь пуста."""
    pass


class OverfullError(Exception):
    """Выбрасывается исключение, когда двухсторонняя очередь переполнена."""
    pass


if __name__ == '__main__':
    number_commands = int(input())
    max_size_deque = Deque(int(input()))
    commands = [input() for _ in range(number_commands)]
    result = []
    for command in commands:
        function, *params = command.split()
        try:
            result = (getattr(max_size_deque, function)(*params))
            if result:
                print(result)
        except OverfullError:
            print('error')
        except EmptyError:
            print('error')
