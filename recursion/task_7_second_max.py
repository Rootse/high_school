def second_max_rec(numbers: list[int], max_values: list[int]) -> int:
    if len(numbers) == 0:
        return max_values[1]

    if numbers[0] > max_values[0]:
        max_values[1], max_values[0] = max_values[0], numbers[0]
    elif numbers[0] > max_values[1]:
        max_values[1] = numbers[0]

    return second_max_rec(numbers[1:], max_values)


def second_max(numbers: list[int]) -> int:
    return second_max_rec(numbers, [numbers[0], numbers[0]])
