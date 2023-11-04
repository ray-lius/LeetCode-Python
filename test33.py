""" 
75. Sort Colors #
题目 #
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example 1:


Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?


sultion 1: greedy - brutal force

build a dict store each color

then exchange each value in the area

sultion 2:



"""


def sort_color(colors: list[int])->list[int]:
    
    zero, one = 0, 0
    
    for idx, color in enumerate(colors):
        colors[idx] = 2
        
        if color <= 1:
            colors[one] = 1
            one += 1
        if color == 0:
            colors[zero] = 0
            zero += 1
    
    return colors
        
test_cases= [[2,0,2,1,1,0]]
print([sort_color(test) for test in test_cases])


nums = [1,2,3,4,5]
nums[0], nums[1] = nums[1], nums[0]
print(nums)

n = nums.pop()
print (n, nums)
