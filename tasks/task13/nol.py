# ID: 52434276

def zero_dists(start, seq):
    """Дистанция до 0"""
    value = '0'
    d = start
    for n in seq:
        if n == value:
            d = 0
        else:
            d += 1
        yield d


input()
numbers = input().split()

to_left = zero_dists(len(numbers), numbers)
to_right = reversed(tuple(zero_dists(len(numbers), reversed(numbers))))

print(*map(min, zip(to_left, to_right)))
