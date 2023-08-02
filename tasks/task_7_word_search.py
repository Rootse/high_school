def WordSearch(l: int, s: str, subs: str) -> list[int]:
    result = [0]
    length = 0
    words = s.split()

    for word in words:
        length += len(word) + 1

        if len(word) > l:
            result.pop(-1)
            result += [1 if word[i:i+l] == subs else 0 for i in range(0, len(word), l)]
            length = len(word) % l
            continue

        if length > l:
            result.append(0)
            length = len(word)

        if word == subs and result[-1] == 0:
            result[-1] = 1

    return result
