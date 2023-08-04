def TheRabbitsFoot(s: str, encode: bool) -> str:
    s: str = s.replace(" ", "")
    res: str = ''
    n: int = len(s)
    rows: int = int(n ** 0.5)
    cols: int = int(n ** 0.5) + bool((n ** 0.5) % 1)
    if rows * cols < n:
        rows += 1
    if encode:
        return " ".join([res.join([s[j * cols + i] if j * cols + i < n else "" for j in range(rows)]) for i in range(cols)])
    k: int = 0
    res: list[str] = [""] * n
    for i in range(cols):
        for j in range(rows):
            if j * cols + i >= n:
                continue
            if k < n:
                res[j * cols + i] = s[k]
                k += 1
    return "".join(res)