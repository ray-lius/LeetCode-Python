"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. 
Assume that there is only one duplicate number, find the duplicate one.

Example 1:


Input: [1,3,4,2,2]
Output: 2

Example 2:


Input: [3,1,3,4,2]
Output: 3


solution :
1) brute force O(n^2)
for i, nums in nums:
 for j in range(i+1, len(nums))
  
 
 2) build a set 


3) fast and slow pointer(no)

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ no sure binary search

"""

def checkRepeatNumber(nums: list[int])->int:
    collection = []
    for num in nums:
        if num in collection:
            return num
        else:
            collection.append(num)
    return -1

# Binary search O(n),  ---- not so understand
def checkRepeatNumber2(nums: list[int])->int:
    low = 0
    high = len(nums)-1

    while low<high :
        mid = low + (high-low)//2
        count = 0


        for num in nums:
            if num<= mid:
                count += 1
        # print (mid, count)
        if count > mid:
            high = mid
        else:
            low = mid + 1

    return low

testCases = [[1,3,4,2,2], [3,1,3,4,2] ]
print([checkRepeatNumber(i) for i in testCases])
print([checkRepeatNumber2(i) for i in testCases])