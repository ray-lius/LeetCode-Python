"""" 
1027. Longest Arithmetic Subsequence

Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.

Note that:

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same value (for 0 <= i < seq.length - 1).
 

Example 1:

Input: nums = [3,6,9,12]
Output: 4
Explanation:  The whole array is an arithmetic sequence with steps of length = 3.
Example 2:

Input: nums = [9,4,7,2,10]
Output: 3
Explanation:  The longest arithmetic subsequence is [4,7,10].
Example 3:

Input: nums = [20,1,15,3,10,5,8]
Output: 4
Explanation:  The longest arithmetic subsequence is [20,15,10,5].

"""
# brute force
class Solution:
    def longestArithSeqLength(self, nums: list[int]) -> int:
        
        self.maxSub = 0
        
        def is_squence(nums: list[int]) -> bool:
            if len(nums) <3:
                return False
            for i in range(2, len(nums)):
                if nums[i] - nums[i-1] != nums[i-1] - nums[i-2]:
                    return False
            return True
        def backtracking(idx: int, sub: list[int]) -> None:
            
            
            if is_squence(sub):
                print(sub[:])
                self.maxSub = max(self.maxSub, len(sub))
                
            if idx == len(nums):
                return 
            # for i in range(idx, len(nums)):
                    
            sub.append(nums[idx])
            backtracking(idx+1, sub)
            sub.pop()
            backtracking(idx+1, sub)
        backtracking(0, [])
        return self.maxSub
    
    
    # need to spend sometimes to under stand this one
    def longestArithSeqLength2(self, nums: list[int]) -> int:
        
        d ={}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                diff = nums[j] - nums[i]
                d[j, diff] = d.get((i, diff), 1) + 1
        print(d)
        return max(d.values())
    
def test_func():
    solution = Solution()
    print(solution.longestArithSeqLength([3,6,9,12]))
    print(solution.longestArithSeqLength([20, 1, 15, 3, 10, 5, 8]))
    
    print(solution.longestArithSeqLength2([3, 6, 9, 12]))
    # print(solution.longestArithSeqLength2([20, 1, 15, 3, 10, 5, 8]))
    testd= {}
    testd[1,2] = 4
    print(testd)
    testd[2,3] = testd.get((4,5),10)
    print(testd)
    

test_func()