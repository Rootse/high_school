def Unmanned(l: int, n: int, track: list[list[int, int, int]]) -> int:
    total_time = 0

    if n == 0:
        return l

    t = [l if t > l else t for t, r, g in track]

    for i in range(n):
        r, g = track[i][1:]

        if t[i] >= l:
            return l

        if i == 0:
            total_time += t[i]
        else:
            total_time += t[i] - t[i - 1]

        cycle_time = r + g
        total_time += r - (total_time % cycle_time) if total_time % cycle_time <= r else 0

    total_time += l - track[-1][0]
    return total_time
