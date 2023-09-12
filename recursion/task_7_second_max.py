from typing import Union


def second_max_rec(numbers: list[int],  max_values: list, idx: int) -> int:
    if len(numbers) <= idx:
        return max_values[1]

    if numbers[idx] > max_values[0]:
        max_values[1], max_values[0] = max_values[0], numbers[idx]
    elif max_values[1] is None or numbers[idx] > max_values[1]:
        max_values[1] = numbers[idx]

    return second_max_rec(numbers, max_values, idx + 1)


def second_max(numbers: list[int]) -> Union[int, None]:
    if len(numbers) < 2:
        return None
    return second_max_rec(numbers, [numbers[0], None], 1)
