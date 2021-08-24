coefficient1, number, coefficient2, coefficient3 = map(int, input().split())


def get_value_at_point(a, x, b, c):
    return a * x ** 2 + b * x + c


print(get_value_at_point(coefficient1, number, coefficient2, coefficient3))
