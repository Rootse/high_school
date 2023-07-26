def odometer(a: list[int]) -> int:
    time, distance = 0, 0
    for i in zip(a[::2], a[1::2]):
        t = i[1] - time
        distance += i[0] * t
        time += i[1]

    return distance


print(odometer([10, 1, 15, 4, 5, 8]))
