def BiggerGreater(input: str) -> str:
    n = len(input)

    if not n:
        return ""

    i = n - 2
    while i >= 0 and input[i] >= input[i + 1]:
        i -= 1

    if i == -1:
        return ""

    j = n - 1
    while input[j] <= input[i]:
        j -= 1

    chars = list(input)
    chars[i], chars[j] = chars[j], chars[i]
    chars[i + 1:] = chars[i + 1:][::-1]

    return "".join(chars)
