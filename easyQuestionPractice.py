""" 
2 sums

"""

def twoSums(nums: list[int], target: int)->list[int]:
    
    nums_dict = {}
    for idx, num in enumerate(nums):
        another = target-num
        if another in nums_dict:
            return [nums_dict[another], idx]
        nums_dict[num] = idx
    return []

test_cases = [[[2, 7, 11, 15], 9]]
print([twoSums(test[0], test[1]) for test in test_cases])