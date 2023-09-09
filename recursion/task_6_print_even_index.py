def print_even_index(arr: list, index=0) -> None:
    if index >= len(arr):
        return

    if index % 2 == 0:
        print(arr[index])

    print_even_index(arr, index + 1)
