# period = 7
period = int(input())
temperature = [int(item) for item in input().split()]
# temperature = [-1, -10, -8, 0, 2, 0, 5]
# temperature = [1, 2, 5, 4, 8]


def main(input_ls):
    weather_ls = [int(el) for el in input_ls]
    count = 0

    for i in range(1, len(weather_ls) - 1):
        print(weather_ls[i])
        if weather_ls[i - 1] < weather_ls[i] > weather_ls[i + 1]:
            count += 1
    try:
        if weather_ls[1]:

            if weather_ls[0] > weather_ls[1]:
                count += 1

            if weather_ls[-2] < weather_ls[-1]:
                count += 1

    except Exception:
        count += 1

    return count


print(main(temperature))
