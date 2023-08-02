def SumOfThe(n: int, data: list[int]) -> int:
    for i in range(n):
        if data[i] == sum(data) - data[i]:
            return data[i]
