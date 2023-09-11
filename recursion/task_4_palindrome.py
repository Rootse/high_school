# def is_palindrome1(s: str) -> bool:
#     if not hasattr(is_palindrome1, '_idx'):
#         is_palindrome1._idx = 0
#
#     s = s.replace(' ', '')
#
#     if is_palindrome1._idx >= len(s) // 2:
#         is_palindrome1._idx = 0
#         return True
#
#     if s[is_palindrome1._idx] != s[len(s) - is_palindrome1._idx - 1]:
#         return False
#
#     is_palindrome1._idx += 1
#     return is_palindrome1(s)
#
#
# def is_palindrome2(s: str, idx: int = None) -> bool:
#     if idx is None:
#         idx = 0
#
#     s = s.replace(' ', '')
#
#     if idx >= len(s) // 2:
#         return True
#
#     if s[idx] != s[len(s) - idx - 1]:
#         return False
#
#     return is_palindrome2(s, idx + 1)


def is_palindrome3(s: str) -> bool:
    s = s.replace(' ', '')

    def is_palindrome_rec(idx: int) -> bool:
        if idx >= len(s) // 2:
            return True
        if s[idx] != s[len(s) - idx - 1]:
            return False
        return is_palindrome_rec(idx + 1)

    return is_palindrome_rec(0)
