def WordSearch(l: int, s: str, subs: str) -> list[int]:
    lines = []
    words = s.split()
    line = ""

    for word in words:
        if len(line) + len(word) <= l:
            line += word + " "
        else:
            # if not line and len(word) > l:
            #     lines += [word[i:i + l] for i in range(0, len(word), l)]
            lines.append(line.strip())
            line = word + " "

    if line:
        lines.append(line.strip())

    print(lines)
    result = []
    for line in lines:
        if subs in line.split():
            result.append(1)
        else:
            result.append(0)
    return result


print(WordSearch(8, "строка разбивается на набор строк через выравнивание по заданной ширине.", "разбивается"))
