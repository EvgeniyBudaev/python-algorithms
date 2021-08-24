number1, number2, number3 = map(int, input().split())


def get_winner(a, b, c):
    if (a % 2 == 0) & (b % 2 == 0) & (c % 2 == 0):
        return "WIN"
    elif (a % 2 == 1) & (b % 2 == 1) & (c % 2 == 1):
        return "WIN"
    else:
        return "FAIL"


print(get_winner(number1, number2, number3))
