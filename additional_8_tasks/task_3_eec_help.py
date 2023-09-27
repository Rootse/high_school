def EEC_help(arr1: list[int], arr2: list[int]) -> bool:
    if len(arr1) != len(arr2):
        return False

    dict1, dict2 = {}, {}

    for i in arr1:
        dict1[i] = dict1.get(i, 0) + 1

    for i in arr2:
        dict2[i] = dict2.get(i, 0) + 1

    return dict1 == dict2
