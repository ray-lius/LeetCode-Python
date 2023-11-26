from collections import defaultdict
def two_sum(nums: list[int], target: int )->list[int]:
    nums_dict = defaultdict()
    # print(nums, target)
    for idx, val in enumerate(nums):
        other = target - val
        if other in nums_dict:
            return [nums_dict[other], idx]
        nums_dict[val]= idx
    print(nums_dict)
    return None



test_cases = [[[2, 7,11,15],9], [[7,11],99]]
print([two_sum(test_case[0], test_case[1]) for test_case in test_cases])


