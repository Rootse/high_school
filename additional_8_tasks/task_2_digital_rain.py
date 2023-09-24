def digital_rain(col: str) -> str:
    count = 0
    counts = {0: -1}
    res = []

    for i, char in enumerate(col):
        if char == '0':
            count -= 1
        else:
            count += 1

        substring_length = i - counts.get(count, i)
        if substring_length >= len(res):
            res = list(col[counts.get(count, i) + 1:i + 1])
        counts.setdefault(count, i)

    return ''.join(res)
