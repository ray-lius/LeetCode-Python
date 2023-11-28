"""

128. Longest Consecutive Sequence #


Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

solution:(greedy)
1. first sort()
2. find all consecutive sequence
3. get max length

O(n)
solution 2:
1. sort()
2. count each secutive sequence, record the max


"""

# O(n logn)
from collections import defaultdict
import sys


def longestConsecutive (nums: list[int]) -> int:
    print(len(nums))
    if(len(nums) == 1):
        return 1
    
    
    nums =  list(set(nums))
    nums.sort()
    print(nums)
    maxLength = 0
    count = 1
    for idx in range(1, len(nums)):
        if nums[idx] - nums[idx-1] == 1:
            count += 1
        else:
            count  = 1
        if count > maxLength:
            maxLength =  count
    return maxLength


def longestConsecutive2 (nums: list[int]) -> int:
    numSet = set(nums)

    print (numSet)
    maxLength = 0
    length = 0
    for num in nums:
        if num -1 not in nums:
            length = 0 
            while (num+length) in numSet:
                length += 1
            maxLength = max(length, maxLength)
    return maxLength


testArray01 = [100,4,200,1,3,2]
testArray02 = [0,3,7,2,5,8,4,6,0,1]
testList = [testArray01, testArray02,  [100,4,200,1,3,2]]
# -1 -1 0


print( 'first function:   ', [longestConsecutive(i) for i in testList ])
print( 'second function 2 : ', [longestConsecutive2(i) for i in testList ])



########### beautiful way to figure it out
#O(n)
######
def longestConsecutive3(nums: list[int]) -> int:
    nums_dict = defaultdict(int)
    maxLength = 0
    
    for idx, num in enumerate(nums):
        print(nums_dict)
        if nums_dict[num] == 0:
            left, right, sum = 0, 0 , 0
            if nums_dict[num-1] > 0:
                left = nums_dict[num-1]
            else:
                left = 0
            if nums_dict[num+1] > 0:
                right = nums_dict[num+1]
            else:
                right = 0
            
            # sum: length of sequence n is in
            sum = right+left+1
            nums_dict[num] = sum
            
            # keep track if max length
            maxLength = max(maxLength, sum)
            
            # extend the length to the boundary(s) of the sequence
			# will do nothing if n has no neighbors
            nums_dict[num-left] = sum
            nums_dict[num+right] = sum
        else:
            continue
            
            
    return maxLength

print('second function 3 : ', [longestConsecutive3(i) for i in testList ])




"""
Given an integer array nums, return the length of the longest strictly increasing 
subsequence
.

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104


solution: dp
if num[i]> num[i-1]
 result[i] =  1+ num[i-1]
else
 result[i] = num[i-1]

"""

# O(n^2)
def lengthOfLIS(nums: list[int])->int:
    LIS = [1]*len(nums)

    for i in range(len(nums)-1, -1, -1):
        for j in range(i+1, len(nums)):
            if nums[i] < nums[j]:
                LIS[i] = max(LIS[i], 1+LIS[j])
    return max(LIS)


#O(n logn)
def longestIncreaseSubsequence(nums: list[int])->int:
    if len(nums) == 0:
        return 0
    dp = [nums[0]]
    for i in range(len(nums)):
        if nums[i]> dp[-1]:
            dp.append(nums[i])
        if nums[i]< dp[-1]:
            for j in range(len(dp)):
                if dp[j]>= nums[i]:
                    dp[j] = nums[i]
                    break
    return len(dp)


test_cases = [[3,2,1,3,2,3,4], [10,9,5,6,3,4,5,6,9,101,18], [0,1,0,3,2,3], [4,10,4,3,8,9]]
print([longestIncreaseSubsequence(val) for val in test_cases])
print([lengthOfLIS(val) for val in test_cases])
# expect 4








""" 

53. Maximum Subarray

Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104



dp  =[]

dp[i] represt the largetst

dp[i] = nums[i]+dp[i -1] (dp[i-1] > 0)
dp[i] = nums[i] (dp[i-1] < 0)
"""
def maxSubArray(nums: list[int]) -> int:
    
    nums_len = len(nums)
    
    if nums_len == 0:
        return 0
    if nums_len == 1:
        return nums[0]

    dp = [0 for _ in nums]
    dp[0], maxSub = nums[0], -sys.maxsize-1
    
    for idx in range(1, nums_len):
        if dp[idx-1]<0:
            dp[idx] = nums[idx]
        else:
            dp[idx] = nums[idx] + dp[idx-1]
        maxSub = max(maxSub, dp[idx])
    return maxSub
    


def maxSubArray2(nums: list[int]) -> int:
    
    nums_len = len(nums)
    
    if nums_len == 0:
        return 0
    if nums_len == 1:
        return nums[0]

    result, maxSum, p = 0, nums[0], 0
    
    while p < nums_len:
        result += nums[p]
        if result > maxSum:
            maxSum = result
        if result < 0:
            result = 0
        p += 1
            
    return maxSum
    

test_cases2= [[-2,1,-3,4,-1,2,1,-5,4], [-2, -1]]
print([maxSubArray(test) for test in test_cases2])
print([maxSubArray2(test) for test in test_cases2])




""" 
def coinChange(self, coins: List[int], amount: int) -> int:
        if amount  == 0:
            return 0
    
        count  = 0
        coins = sorted(coins, reverse=True)
        for coin in coins:
            if coin > amount:
                continue
            elif coin == amount:
                count  += 1
                amount  = 0
            else:
                count  += amount//coin
                amount = amount%coin
        
            if amount == 0:
                break

        if amount != 0:
            return -1

        return count

"""