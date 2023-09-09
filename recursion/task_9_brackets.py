def brackets1(n: int) -> list[str]:
    if n == 0:
        return ['']

    result = []
    for i in range(n):
        for left in brackets1(i):
            for right in brackets1(n - i - 1):
                result.append(f'({left}){right}')
    return result


def gen_brackets(result: list[str], left: int, right: int, brackets: list[str], count: int) -> None:
    if left < 0 or right < left:
        return

    if left == 0 and right == 0:
        result.append(''.join(brackets))
        return

    if left > 0:
        brackets[count] = '('
        gen_brackets(result, left - 1, right, brackets, count + 1)

    if right > left:
        brackets[count] = ')'
        gen_brackets(result, left, right - 1, brackets, count + 1)


def brackets2(n: int) -> list[str]:
    result = []
    gen_brackets(result, n, n, [''] * n * 2, 0)
    return result
