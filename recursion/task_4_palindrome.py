def is_palindrome(s: str, start: int = 0, end: int = -1) -> bool:
    s = s.replace(' ', '')
    if start == len(s) // 2:
        return True

    if s[start] != s[end]:
        return False

    return is_palindrome(s, start + 1, end - 1)
