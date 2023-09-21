def white_walkers(village: str) -> bool:
    nums = []
    equals = 0

    for char in village:
        if char.isdigit():
            nums.append(int(char))

        if char == '=':
            equals += 1

        if len(nums) >= 2 and nums[-1] + nums[-2] == 10:
            if equals < 3:
                return False

            nums.append(nums[-1])
            equals = 0

    return len(nums) > 1
