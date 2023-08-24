def create_rings(matrix, m, n):
    rings = []

    for i in range(min(m, n) // 2):
        ring = []

        for j in range(i, n - i):
            ring.append(int(matrix[i][j]))

        for j in range(i + 1, m - i - 1):
            ring.append(int(matrix[j][n - i - 1]))

        for j in range(n - i - 1, i - 1, -1):
            ring.append(int(matrix[m - i - 1][j]))

        for j in range(m - i - 2, i, -1):
            ring.append(int(matrix[j][i]))

        rings.append(ring)

    return rings


def convert_to_matrix(rings, m, n):
    matrix = [[''] * n for _ in range(m)]

    for i in range(min(m, n) // 2):
        ring = rings[i]

        for j in range(i, n - i):
            matrix[i][j] = str(ring.pop(0))

        for j in range(i + 1, m - i - 1):
            matrix[j][n - i - 1] = str(ring.pop(0))

        for j in range(n - i - 1, i - 1, -1):
            matrix[m - i - 1][j] = str(ring.pop(0))

        for j in range(m - i - 2, i, -1):
            matrix[j][i] = str(ring.pop(0))

    return [''.join(row) for row in matrix]


def MatrixTurn(matrix: list[str], m: int, n: int, t: int) -> None:
    rings = create_rings(matrix, m, n)


    matrix = convert_to_matrix(rings, m, n)

    # temp_matrix = [[matrix[x][y] for y in range(n)] for x in range(m)]
    # print(temp_matrix)
    # for _ in range(t):
    #     for i in range(m // 2):
    #         for j in range(i, n - i - 1):
    #             # print(i, j, m, n)
    #             # print(n - j - 1)
    #             # print(n - i - 1)
    #             temp = temp_matrix[i][j]
    #             print(temp)
    #             temp_matrix[i][j] = temp_matrix[m - j - 1][i]
    #             print(temp_matrix)
    #             temp_matrix[m - j - 1][i] = temp_matrix[m - i - 1][n - j - 1]
    #             print(temp_matrix)
    #             temp_matrix[m - i - 1][n - j - 1] = temp_matrix[j][n - i - 1]
    #             print(temp_matrix)
    #             temp_matrix[j][n - i - 1] = temp
    #             print()
    #
    # for i in range(m):
    #     for j in range(n):
    #         matrix[i][j] = temp_matrix[i][j]


matrix = ["123456", "234567", "345678", "456789"]
print(MatrixTurn(matrix, 4, 6, 3))
