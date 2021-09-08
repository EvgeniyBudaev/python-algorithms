# Перебираем А строку.
# Делаем поиск в Б. Если есть удаляем в Б если нет добавляем в результат.
# И в конце все что осталось от строки тоже добавляем в результат
# (на случай если перебирали короткую строку )

# str1 = 'xtkpx'
# str2 = 'xkctpx'

str1 = input()
str2 = input()


def diff(a, b):
    s = list(b)
    res = ""
    for i in a:
        try:
            x = s.index(i)
        except ValueError:
            res += i
        else:
            s.pop(x)
    res += "".join(s)
    return res


print(diff(str1, str2))
