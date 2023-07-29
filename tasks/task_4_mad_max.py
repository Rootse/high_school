def MadMax(n: int, tele: list[int]):
    tele.sort()
    mid = n // 2
    tele[mid], tele[-1] = tele[-1], tele[mid]
    left = tele[:mid]
    right = tele[mid + 1:]
    right.sort(reverse=True)
    return left + [tele[mid]] + right
