def create_rings(matrix: list[str], m: int, n: int) -> list[list[int]]:
    rings = []
    for i in range(min(m, n) // 2):
        ring = [int(matrix[i][j]) for j in range(i, n - i)]
        ring += [int(matrix[j][n - i - 1]) for j in range(i + 1, m - i - 1)]
        ring += [int(matrix[m - i - 1][j]) for j in range(n - i - 1, i - 1, -1)]
        ring += [int(matrix[j][i]) for j in range(m - i - 2, i, -1)]

        rings.append(ring)

    return rings


def convert_to_matrix(rings: list[list[int]], m: int, n: int) -> list[str]:
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


def shift(arr: list[int], t: int) -> None:
    t %= len(arr)
    if not t:
        return
    arr[:t], arr[t:] = arr[-t:], arr[:-t]


def MatrixTurn(matrix: list[str], m: int, n: int, t: int) -> None:
    rings = create_rings(matrix, m, n)

    for i in range(len(rings)):
        shift(rings[i], t)

    matrix[:] = convert_to_matrix(rings, m, n)
