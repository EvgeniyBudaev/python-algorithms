B. Список дел

Васе нужно распечатать свой список дел на сегодня. Помогите ему: напишите функцию, которая печатает все его дела. Известно, что дел у Васи не больше 5000.
Внимание: в этой задаче не нужно считывать входные данные. Нужно написать только функцию, которая принимает на вход голову списка и печатает его элементы. Ниже дано описание структуры, которая задаёт узел списка. Используйте компилятор Make.
Мы рекомендуем воспользоваться заготовками кода для данной задачи, расположенными по ссылке.
Решение надо отправлять только в виде файла с расширением, которое соответствует вашему языку. Иначе даже корректно написанное решение не пройдет тесты.

Формат ввода<br>
В качестве ответа сдайте только код функции, которая печатает элементы списка. Длина списка не превосходит 5000
элементов. Список не бывает пустым.
Следуйте следующим правилам при отправке решений:

1. Нужно выбирать компилятор Make.
2. Решение нужно отправлять в виде файла с расширением соответствующем вашему языку программирования.
3. Для Java файл должен называться Solution.java
4. Для остальных языков программирования это имя использовать нельзя (имя «solution» тоже).
5. Для Go укажите package main.

Python:<br>
Если вы пишете на Python, функция должна принимать на вход вершину node и иметь сигнатуру

solution(node) -> None
Узел списка описывается следующим классом:

class Node:  
    def __init__(self, value, next_item=None):  
        self.value = value  
        self.next_item = next_item

Формат вывода<br>
Функция должна напечатать элементы списка по одному в строке.
