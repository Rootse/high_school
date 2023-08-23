def SherlockValidString(s: str) -> bool:
    freq = {}
    for letter in s:
        freq[letter] = freq.get(letter, 0) + 1

    values = list(freq.values())
    print(values)
    return (max(values) == min(values) or
            (max(values) - 1 == min(values) and values.count(min(values)) == 1) or
            (min(values) + 1 == max(values) and values.count(max(values)) == 1))
