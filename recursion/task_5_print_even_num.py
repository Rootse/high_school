def print_even_num(numbers: list[int], index: int = 0) -> None:
    if len(numbers) <= index:
        return

    if numbers[index] % 2 == 0:
        print(numbers[index])

    print_even_num(numbers, index + 1)
