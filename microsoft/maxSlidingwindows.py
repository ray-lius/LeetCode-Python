""" 
239. Sliding Window Maximum

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
"""



from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        
        if len(nums) <= k:
            return [max(nums)]
        slideWindow = deque([])
        maxStack = []
        
        
        for i in range(len(nums)):
            if i<k:
                slideWindow.append(nums[i])
                if i == k-1:
                    # print(slideWindow, max(slideWindow))
                    maxStack.append(max(slideWindow))
            else:
                slideWindow.append(nums[i])
                slideWindow.popleft()
                maxStack.append(max(slideWindow))
        
        return maxStack
    
    
def test_func():

    solution = Solution()
    print(solution.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))

    solution2 = Solution()
    print(solution2.maxSlidingWindow(nums=[1], k=1))


test_func()
