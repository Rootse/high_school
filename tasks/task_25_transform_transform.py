def S(a: list[int]) -> list[int]:
    b = []
    for i in range(len(a)):
        for j in range(len(a) - i):
            k = i + j
            b.append(max(a[j:k + 1]))
    return b


def TransformTransform(a: list[int], n: int) -> bool:
    return sum(S(S(a))) % 2 == 0
