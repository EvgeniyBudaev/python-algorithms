# 53351169

def quick_sort(array):
    """Эффективная быстрая сортировка."""
    def partition(left, right):
        pivot = array[right]
        divider = left-1
        for current in range(left, right):
            if array[current] < pivot:
                divider += 1
                array[divider], array[current] = (array[current],
                                                  array[divider])
        array[divider + 1], array[right] = (array[right],
                                            array[divider + 1])
        return divider + 1

    def quick_sort_internal(left, right):
        """Внутренняя быстрая сортировка."""
        if right <= left:
            return
        divider = partition(left, right)
        quick_sort_internal(left, divider - 1)
        quick_sort_internal(divider + 1, right)
    quick_sort_internal(0, len(array)-1)
    return array


if __name__ == '__main__':
    """В первой строке задается число участников. В каждой из следующих n 
    строк задана информация про одного из участников. i-й участник 
    описывается тремя параметрами: уникальным логином,числом решённых задач, 
    штрафом."""
    length = int(input())
    players = [(lambda login, task_count, fine: (-int(task_count),
                                                int(fine),
                                                login))(*input().split(' '))
               for _ in range(length)]
    quick_sort(players)
    print(*[player[2] for player in players], sep='\n')
