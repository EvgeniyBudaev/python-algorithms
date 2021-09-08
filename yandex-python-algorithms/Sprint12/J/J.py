number = int(input())


def get_factorial(n):
    container = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            container.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        container.append(n)
    result = ' '.join(map(str, container))
    return result


print(get_factorial(number))
