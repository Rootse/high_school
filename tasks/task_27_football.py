def Football(f: list[int], n: int) -> bool:
    for i in range(n):
        for j in range(i + 1, n):
            f[i], f[j] = f[j], f[i]
            if sorted(f) == f:
                return True
            f[i], f[j] = f[j], f[i]

    for i in range(n):
        for j in range(i + 2, n):
            f[i:j + 1] = f[i:j + 1][::-1]
            if sorted(f) == f:
                return True
            f[i:j + 1] = f[i:j + 1][::-1]

    return False
