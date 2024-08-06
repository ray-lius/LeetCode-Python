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
    
# last practice on 06 Aug 2024

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

