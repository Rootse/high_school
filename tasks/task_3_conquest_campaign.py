def check_cell(x: int, y: int, w: int, h: int) -> bool:
    if 0 <= x <= h and 0 <= y <= w:
        return True

    return False


def add_captured_cell(captured_cells: list[tuple[int, int]], x: int, y: int, w: int, h: int) -> list[tuple[int, int]]:
    if not check_cell(x, y, w, h):
        return captured_cells
    captured_cells.append((x, y))

    return captured_cells


def ConquestCampaign(n: int, m: int, l: int, battalion: list[int]) -> int:
    day = 0
    field = [(x, y) for y in range(1, n + 1) for x in range(1, m + 1)]

    captured_cells = []
    for y, x in zip(battalion[::2], battalion[1::2]):
        captured_cells.append((y, x))
    else:
        day += 1

    while not set(field).issubset(captured_cells):

        for i in range(len(captured_cells)):
            x, y = captured_cells[i]
            captured_cells = add_captured_cell(captured_cells, x+1, y, n, m)
            captured_cells = add_captured_cell(captured_cells, x, y+1, n, m)
            captured_cells = add_captured_cell(captured_cells, x-1, y, n, m)
            captured_cells = add_captured_cell(captured_cells, x, y-1, n, m)

        day += 1

    return day
