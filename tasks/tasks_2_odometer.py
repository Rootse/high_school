def odometer(a: list[int]) -> int:
    time, distance = 0, 0
    for i in zip(a[::2], a[1::2]):
        time = i[1] - time
        distance += i[0] * time
        time = i[1]

    return distance