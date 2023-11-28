"""

35. Search Insert Position


Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4




"""
######################################################################
# must conquer the binary search
######################################################################


import heapq
import random


def searchInsert( nums: list[int], target: int) -> int:

        n = len(nums)
        left, right = 0, n-1
        while left <= right:
            middle = left + (right-left)//2
            if nums[middle] >= target:
                right = middle-1
            else:
                if middle == n-1 or nums[middle+1]>=target:
                    return middle + 1 
                left = middle + 1


        return 0
    
test_cases = [[[1,3,5,6], 5]]


print([ searchInsert(test[0], test[1]) for test in test_cases])


"""

74. Search a 2D Matrix

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.


example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:

example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false


"""
###########################################
# 经典二分查找，！！！！！！！！！！！重要！！！！#
###########################################
def searchByBinary(nums: list[int], target: int)->bool:
        n = len(nums)
        left, right = 0, n-1
        while left <= right:
            middle = left + (right-left)//2
            if nums[middle] == target:
                return True
            elif nums[middle]> target:
                right = middle-1
            else:
                left = middle + 1
        return False

def searchMatrix(matrix: list[list[int]], target: int) -> bool:
        
        # brute force
        # for each in matrix:
        #     if each[0]<= target and each[-1] >= target:
        #         return searchByBinary(each, target)
        
        # need search in binary
        n = len(matrix)
        left, right = 0, n-1

        if target >= matrix[-1][0]:
            return searchByBinary(matrix[-1], target)
        
        while left < right:

            if right -left == 1:
                 return searchByBinary(matrix[left], target)

            middle = left + (right-left)//2

            if matrix[middle][0] == target:
                return True
            elif matrix[middle][0] > target:
            
                right = middle
            else:
                left = middle

        return False



def searchMatrix2(matrix: list[list[int]], target: int)->bool:
        
        if len(matrix) == 0:
            return False
        
        m, low, high = len(matrix[0]), 0, len(matrix)*len(matrix[0])-1
        while low <= high:
            
            middle = low + (high-low)//2
            if matrix[middle//m][middle%m] == target:
                return True
            elif matrix[middle//m][middle%m] > target:
                high = middle -1
            else:
                low = middle + 1

        return False



test_cases2 = [[[[1,3,5,7],[10,11,16,20],[23,30,34,50]], 11], [[[1],[3]], 3]]

print([searchMatrix(test[0], test[1]) for test in test_cases2])

print([searchMatrix2(test[0], test[1]) for test in test_cases2])



"""

215. Kth Largest Element in an Array

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4



"""


def findKthLargest(nums: list[int], k: int)->int:
    nums.sort()
    return nums[-k]




######################################
####### use heap in python
######################################
def findKthLargest3(nums: list[int], k: int)->int:
    heap = nums[:k]
    heapq.heapify(heap)
    
    
    for num in nums[k:]:
        if num>heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, num)
    
    
    return heap[0]

def findKthLargest4(nums: list[int], k: int)->int:
     heap = nums[:k]
     heapq.heapify(heap)
     
     for num in nums[k:]:
          heapq.heappushpop(heap, num)
          #heapq.heapreplace(heap, num)
    
     return heap[0]


# these two method will use the sorted method , O(n logn)
def findKthLargest5(nums: list[int], k: int)->int:
     
     res = heapq.nlargest(k , nums )
     print('lllllll',res)
     return res[-1]

##### to return the kth smallest list of nums, use sort method O(n logn)
def findKthSmallest6(nums: list[int], k: int)->int:
     
     res = heapq.nsmallest(k , nums )
     print('ssssssssss',res)

     return res[-1]



#########################################################
# Quick select function
# this function is for Partion and binart search!!!!
# not recommend
########################################################
def partition(nums: list[int], left: int, right: int)->int:
     k = left + random.random(right-left+1)

     nums[k], nums[right] = nums[right], nums[k]
     i = left-1

     for j in range(left, right):
          if nums[j] <= nums[right]:
               i += 1
               nums[i], nums[j] = nums[j], nums[i]
               
     nums[i+1], nums[right] = nums[right], nums[i+1]
     return i + 1

def selectSmallest(nums: list[int], left: int, right: int, i: int)->int:
     
    if left >= right:
         return nums[left]
    
    q = partition(nums, left, right)

def findKthLargest1(nums: list[int], k: int)->int:
     for num in nums:
          if nums > 0:
               return num
     return -1
    
    


test_cases3 = [[[3,2,1,5,6,4], 2], [[3,2,3,1,2,4,5,5,6], 4]]
print([findKthLargest(test[0], test[1]) for test in test_cases3])
print([findKthLargest3(test[0], test[1]) for test in test_cases3])
print([findKthLargest4(test[0], test[1]) for test in test_cases3])
print([findKthLargest5(test[0], test[1]) for test in test_cases3])
print([findKthSmallest6(test[0], test[1]) for test in test_cases3])