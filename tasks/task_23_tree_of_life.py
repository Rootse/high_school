def TreeOfLife(h: int, w: int, n: int, tree: list) -> list:
    work_tree = [[0 if cell == "." else 1 for cell in row] for row in tree]

    for generation in range(n):
        work_tree = [[cell + 1 for cell in row] for row in work_tree]
        if generation % 2 == 0:
            continue

        new_tree = work_tree
        positions = [(x, y) for y in range(w) for x in range(h) if work_tree[x][y] > 2]
        for x, y in positions:
            positions = [(x, y), (x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]
            for pos_x, pos_y in positions:
                if 0 <= pos_x < h and 0 <= pos_y < w:
                    new_tree[pos_x][pos_y] = 0

        work_tree = new_tree

    tree = ["".join("+" if cell > 0 else "." for cell in row) for row in work_tree]

    return tree
