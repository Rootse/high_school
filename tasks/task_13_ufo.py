def UFO(n: int, data: list[int], octal: bool) -> list[int]:
    if octal:
        return [int(str(i), 8) for i in data]

    return [int(str(i), 16) for i in data]
