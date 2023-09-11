def print_even_num(numbers: list[int]) -> None:
    def print_even_num_rec(idx: int) -> None:
        if len(numbers) <= idx:
            return

        if numbers[idx] % 2 == 0:
            print(numbers[idx])

        print_even_num_rec(idx + 1)

    print_even_num_rec(0)
