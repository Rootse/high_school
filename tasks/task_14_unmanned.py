def Unmanned(l: int, n: int, track: list[list[int, int, int]]) -> int:
    total_time = 0

    if n == 0:
        return l

    for i in range(n):
        t, r, g = track[i]

        if i == 0:
            total_time += t
        else:
            total_time += t - track[i - 1][0]

        cycle_time = r + g
        total_time += r - (total_time % cycle_time) if total_time % cycle_time <= r else 0

    total_time += l - track[-1][0]
    return total_time
