def Keymaker(k: int) -> str:
    return ''.join('1' if int(i ** 0.5) ** 2 == i else '0' for i in range(1, k + 1))
