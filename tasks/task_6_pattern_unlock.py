def PatternUnlock(n: int, hits: list[int]) -> str:
    coords = {1: (2, 1), 2: (2, 2), 3: (2, 3), 4: (1, 3), 5: (1, 2), 6: (1, 1), 7: (3, 3), 8: (3, 2), 9: (3, 1)}

    length = 0
    for i in range(n - 1):
        x1, y1 = coords[hits[i]]
        x2, y2 = coords[hits[i + 1]]
        length += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return str(int(length * 100000 + 0.5)).replace('0', '')
