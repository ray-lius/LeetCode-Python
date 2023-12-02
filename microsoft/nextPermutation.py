""" 
31. Next Permutation

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
"""


class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <2:
            return nums
        
        # position of last decrease
        decrease_pos = len(nums) -2
        while decrease_pos and nums[decrease_pos] >= nums[decrease_pos+1]:
            decrease_pos -= 1
        
        if decrease_pos == 0:
            nums.sort()
            return
        
        # postion need to change
        change_pos = len(nums) -1
        while nums[change_pos] < nums[decrease_pos]:
            change_pos -= 1
        
        nums[decrease_pos], nums[change_pos] = nums[change_pos], nums[decrease_pos]
    
    
    
    




def permuation(nums: list[int]) ->list[list[int]]:
    
    comb = []
    
    def recursor(ans: list[int], nums: list[int])->None:
        
        if not nums:
            comb.append(ans[:]) # add contanier cpoy to result
            return
        
        for i in range(len(nums)):
            ans.append(nums[i])
            recursor(ans, nums[:i] + nums[i+1:])
            ans.pop()
            
    recursor([], nums)
    return comb
        
def test_func():
    
    print(permuation([1, 2, 3]))
    print(permuation([1, 1, 5]))
    
    test = [1, 2, 3]
    print(test)
    solution = Solution()
    solution.nextPermutation(test)
    print(test)
    
    test = [3,2,1]
    print(test)
    solution = Solution()
    solution.nextPermutation(test)
    print(test)
    
    test = [1, 1, 5]
    print(test)
    solution = Solution()
    solution.nextPermutation(test)
    print(test)
    
test_func()
