def degree(n: int, m: int) -> int:
    if m == 0:
        return 1

    return n * degree(n, m - 1)
