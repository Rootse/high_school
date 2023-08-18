def MisterRobot(n: int, data: list[int]) -> bool:
    for i, num in enumerate(data):
        if 0 < i < n - 1:
            if (i + 1) % 2 != num % 2 and not (data[i + 1] == num + 1 or data[i - 1] == num - 1):
                return False
        elif i == 0:
            if (i + 1) % 2 != num % 2 and not (data[i + 1] == num + 1):
                return False
        else:
            if (i + 1) % 2 != num % 2 and not (data[i - 1] == num - 1):
                return False

    return True
