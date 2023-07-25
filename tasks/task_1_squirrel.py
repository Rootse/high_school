def factorial(n: int) -> int:
    if n < 2:
        return 1

    return factorial(n - 1) * n


def squirrel(n: int) -> int:
    return int(str(factorial(n))[0])

