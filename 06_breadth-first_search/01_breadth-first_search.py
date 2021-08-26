from collections import deque


def person_is_seller(name):
    # Функция проверяет, заканчивается ли имя на букву 'm',
    # и если заканчивается, этот человек считается продавцом манго.
      return name[-1] == 'm'


graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def search(name):
    # Создание новой двусторонней очереди (дека)
    search_queue = deque()
    # Все соседи добавляются в очередь поиска
    search_queue += graph[name]
    # Этот массив используется для отслеживания уже проверенных дюдей
    searched = set()
    # Пока очередь не пуста...
    while search_queue:
        # Из очереди извлекается первый человек
        person = search_queue.popleft()
        # Человек проверяется только в ом случае, если он не проверялся ранее
        if person not in searched:
            # Проверяем, является ли этот человек продавцом манго
            if person_is_seller(person):
                # Да, это продавец манго
                print(person + " is a mango seller!")
                return True
            else:
                # Нет, не является.
                # Все друзья этого человека добавляются в очередь поиска
                search_queue += graph[person]
                # Человек помечается как уже провереный
                searched.add(person)
    # Если выполнение дошло до этой строки, значит, в очереди нет продаца манго
    return False


search("you")
