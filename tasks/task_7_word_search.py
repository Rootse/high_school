def WordSearch(l: int, s: str, subs: str) -> list[int]:
    r = [[0, 0]]
    words = s.split()

    for word in words:
        r[-1][0] += len(word) + 1
        i = 1 if word == subs else 0

        if len(word) > l:
            r += [[0, i] for _ in range(int(-1 * (len(word) / l) // 1 * -1))]
            r[-1][0] = len(word) % l
            continue

        if r[-1][0] > l:
            r.append([len(word) + 1, i])

    return [i for _, i in r]

