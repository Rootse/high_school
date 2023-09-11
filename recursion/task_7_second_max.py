def second_max_rec(numbers: list[int],  max_values: list, idx: int) -> int:
    if len(numbers) <= idx:
        return max_values[1]

    if max_values[0] is None or numbers[idx] > max_values[0]:
        max_values[1], max_values[0] = max_values[0], numbers[idx]
    elif max_values[1] is None or numbers[idx] > max_values[1]:
        max_values[1] = numbers[idx]

    return second_max_rec(numbers, max_values, idx + 1)


def second_max(numbers: list[int]) -> int:
    if len(numbers) == 1:
        return numbers[0]
    return second_max_rec(numbers, [None, None], 0)
