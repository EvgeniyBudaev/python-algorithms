rows = 2
columns = 2

matrix = []

for _ in range(rows):
    matrix.append(list(map(int, input().rstrip().split())))

print(matrix)


def get_adjacent_indices(i, j, m, n):
    n_list = []
    if i > 0:
        n_list.append((matrix[i - 1][j]))
    if i + 1 < m:
        n_list.append((matrix[i + 1][j]))
    if j > 0:
        n_list.append((matrix[i][j - 1]))
    if j + 1 < n:
        n_list.append((matrix[i][j + 1]))
    return ' '.join(map(str, sorted(n_list)))


coordinateX = 1
coordinateY = 0


print(get_adjacent_indices(coordinateX, coordinateY, rows, columns))
