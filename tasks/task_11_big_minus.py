def BigMinus(s1: str, s2: str) -> str:
    res = ""
    carry = 0
    for i in range(min(len(s1), len(s2))):
        if ord(s1[i]) < ord(s2[i]):
            s1, s2 = s2, s1

    i, j = len(s1) - 1, len(s2) - 1
    while i >= 0 or j >= 0:
        x = int(s1[i]) if i >= 0 else 0
        y = int(s2[j]) if j >= 0 else 0
        z = x - y - carry

        if z < 0:
            z += 10
            carry = 1
        else:
            carry = 0

        res = str(z) + res
        i -= 1
        j -= 1

    while res[0] == "0" and len(res) > 1:
        res = res[1:]

    return res