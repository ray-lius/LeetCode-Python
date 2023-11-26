from typing import Optional


def fab(n: int) -> int:
    if n == 0 or n == 1:
        return n
    return fab(n-1) + fab(n-2)

print(fab(2))
print(fab(4))

def buddyStrings(s: str, goal: str) -> bool:
    s_arr, goal_arr = list(s), list(goal)
    
    # print(s_arr, goal_arr)
    
    if len(s_arr) != len(goal_arr):
        return False
    
    count = 0
    for i in range(len(s)):
        if s_arr[i] != goal_arr[i]:
            count += 1
        if count >2:
            return False
    
    return True

print(buddyStrings('abcd', 'cbad'))
print(buddyStrings('ab', 'ba'))

class Solution: 
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx1, idx2 , comb = m-1, n-1, m+n-1
        while idx2 >= 0:
            if idx1 > 0 and nums1[idx1] > nums2[idx2]:
                nums1[comb] = nums1[idx1]
                idx1 -= 1
            else:
                nums1[comb] = nums2[idx2]
                idx2 -= 1
            comb -= 1

def merge_test():
    test1 = [1, 2, 3, 0, 0, 0]
    solution = Solution()
    solution.merge(test1, 3, [2,5,6], 3)
    print(test1)

merge_test()

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution2:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if root == None:
            return False
        
        if root.left == None and root.right == None:
            if targetSum == root.val:
                return True
            else: 
                return False
        
        return self.hasPathSum(root.left, targetSum-root.value) or self.hasPathSum(root.right, targetSum-root.value)
    
    

def climbStairs(n: int) -> int:
    if n==1 or n==2:
        return n
    
    return climbStairs(n-1) + climbStairs(n-2)

print(climbStairs(2))
print(climbStairs(3))

def maxProfit(prices: list[int]) -> int:
    
    maxProfit = 0
    buy = prices[0]
    
    for sell in prices[2:]:
        if sell > buy:
            maxProfit = max(maxProfit, sell-buy)
        else:
            buy = sell
            
    return maxProfit