def print_even_num(numbers: list[int]) -> None:
    if not numbers:
        return

    num = numbers.pop(0)

    if num % 2 == 0:
        print(num)

    print_even_num(numbers)
