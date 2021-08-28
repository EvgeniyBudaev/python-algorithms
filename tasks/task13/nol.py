# ID: 52461815

def zero_dists(start, seq):
    """Дистанция до нуля."""
    value = '0'
    d = start
    for n in seq:
        if n == value:
            d = 0
        else:
            d += 1
        yield d


def distance_counter(values: list[str]):
    """Счетчик дистанции до нуля."""
    to_left = zero_dists(len(values), values)
    to_right = reversed(tuple(zero_dists(len(values), reversed(values))))
    return map(min, zip(to_left, to_right))


def main(values: list[str]):
    return distance_counter(values)


if __name__ == '__main__':
    input()
    numbers = input().split()
    result = main(numbers)
    print(*result)
