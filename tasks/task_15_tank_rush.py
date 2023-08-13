def TankRush(h1: int, w1: int, s1: str, h2: int, w2: int, s2: str) -> bool:
    source_map = [[int(num) for num in row] for row in s1.split()]
    search_map = [[int(num) for num in row] for row in s2.split()]

    for i in range(h1 - h2 + 1):
        for j in range(w1 - w2 + 1):
            if source_map[i][j:j+w2] == search_map[0] and all(source_map[i+x][j:j+w2] == search_map[x] for x in range(1,h2)):
                return True
    return False
