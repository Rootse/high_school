def ConquestCampaign(n: int, m: int, l: int, battalion: list[int]) -> int:
    if n * m <= l:
        return 1

    captured_cells = [(y, x) for y, x in zip(battalion[::2], battalion[1::2])]

    for i in range(l):
        y, x = captured_cells[i]
        if 0 < y + 1 <= m:
            captured_cells.append((y+1, x))
        if 0 < y - 1 <= m:
            captured_cells.append((y-1, x))
        if 0 < x + 1 <= n:
            captured_cells.append((y, x+1))
        if 0 < x - 1 <= n:
            captured_cells.append((y, x-1))

    captured_cells = list(set(captured_cells))
    battalion = [num for tup in captured_cells for num in tup]
    return ConquestCampaign(n, m, len(captured_cells), battalion) + 1