def white_walkers(village: str) -> str:
    nums = []
    equals = 0
    res = []

    for char in village:
        if char.isdigit():
            nums.append(int(char))

        if char == '=':
            equals += 1

        if len(nums) >= 2 and nums[-1] + nums[-2] == 10 and equals < 3:
            equals = 0
            res.append(False)

        if len(nums) >= 2 and nums[-1] + nums[-2] == 10 and equals >= 3:
            nums.append(nums[-1])
            equals = 0

    if len(nums) <= 1:
        return False

    return all(res)
