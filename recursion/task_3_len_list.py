def len_list(l: list) -> int:
    if not l:
        return 0

    l.pop(0)
    return 1 + len_list(l)
