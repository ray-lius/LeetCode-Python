"""


4. Median of Two Sorted Arrays
Hard
25.6K
2.8K
Companies
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106


"""





from heapq import merge
import heapq

#
# the key thing is find a way to get the thing done with O(log(m+n)) not O(m+n)
#
def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
    pass








"""
below is the ways to combine two sorted array


"""
# extra knowldge
# O(m+n)
def mergeTwoSortedList(list1: list[int], list2: list[int])->list[int]:
    result = []
    i = j = 0
    n1 = len(list1)
    n2 = len(list2)
    while i < n1 and j < n2:
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    result = result + list1[i:] + list2[j:]
    return result

test_list1 = [1, 5, 6, 9, 11]
test_list2 = [3, 4, 7, 8, 10]


# 1
res = sorted(test_list1 + test_list2)

print ("1. The combined sorted list is : " + str(res))

#2
res = list(merge(test_list1, test_list2))

print ("2. The combined sorted list is : " + str(res))

#3


print ("3. The combined sorted list is : " + str(mergeTwoSortedList(test_list1, test_list2)))

#4 --- this will change the list1
test_list1.extend(test_list2)
test_list1.sort()

print ("4. The combined sorted list is : " + str(res))




""" 

373. Find K Pairs with Smallest Sums
You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

 

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [[1,3],[2,3]]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]

"""

def kSmallestPairs(nums1: list[int], nums2: list[int], k: int)->list[list[int]]:
    result = []
    hq = []
    
    if len(nums1) * len(nums2) < k:
        k = len(nums1) * len(nums2) 
        
    for idx, num in enumerate(nums1):
        heapq.heappush(hq, [num, nums2[0], 0])
    
    while len(result) < k:
        min_res = heapq.heappop(hq)
        result.append(min_res[:2])
        if min_res[2] < len(nums2)-1:
            heapq.heappush(hq, [min_res[0], nums2[min_res[2]+1], min_res[2]+1])
    return result

def kSmallestPairs2(nums1: list[int], nums2: list[int], k: int)->list[list[int]]:
    result = []
    hq = []
    
    if len(nums1) * len(nums2) < k:
        k = len(nums1) * len(nums2) 
        
    for idx, num in enumerate(nums1):
        heapq.heappush(hq, [num+nums2[0], 0])
    
    while len(result) < k:
        min_res = heapq.heappop(hq)
        result.append([min_res[0]-nums2[min_res[1]], nums2[min_res[1]]])
        if min_res[1] < len(nums2)-1:
            heapq.heappush(hq, [min_res[0]-nums2[min_res[1]]+nums2[min_res[1]+1], min_res[1]+1])
    return result


test_cases = [[[1,7,11], [2,4,6], 3], [[1,1,2], [1,2,3], 2], [[1,2], [3], 3]]
print([kSmallestPairs(test[0], test[1], test[2]) for test in test_cases])

print([kSmallestPairs2(test[0], test[1], test[2]) for test in test_cases])