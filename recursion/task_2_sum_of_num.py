def sum_of_num(num: int) -> int:
    if 0 <= num <= 9:
        return num

    return (num % 10) + sum_of_num(num // 10)
