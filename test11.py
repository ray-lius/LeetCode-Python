"""
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


solution:
slide windows (brute force)
1) for each char: calcu the longestest the substring, no repeaet char



solution2:
slide window: 
with flex start and end
whenever get same, we cut off the slide window

solution3:


"""
# O(n^2)
# n-1 + n-2 + n-3 + ..... n-n = n^2 - (1+2+....n) = n^2 - 1/2n(n+1) = 1/2n^2 - 1/2
def longestNoRepeatSubstring(s: str)->int:
    longestStr = 1
    for idx in range(len(s)):
        for i in range(1, len(s)-idx):
            if s[idx+i] not in s[idx: idx+i]:
                longestStr = max(longestStr, i+1)
            else:
                break

    return longestStr



# use set to record current window
def longestNoRepeatSubstring2(s: str)->int:
    length = len(s)
    maxLength = 0
    charSet = set()
    left = 0
    for right in range(length):
        if s[right] not in charSet:
            charSet.add(s[right])
            maxLength = max(maxLength, right-left+1)
        else:
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])

    return maxLength

# use slice to get the current slide window
def longestNoRepeatSubstring3(s: str)->int:
    length = len(s)
    maxLength = 0
    
    left = 0
    for right in range(1, length):
        if s[right] not in s[left:right]:
            #charSet.add(s[right])
            maxLength = max(maxLength, right-left+1)
        else: 
            left = s[left:right].find(s[right])+1

    return maxLength

# use slice to get the current slide window
# use charMap to rememebr the char relative position
def longestNoRepeatSubstring4(s: str)->int:
    length = len(s)
    maxLength = 0
    charMap ={}
    left = 0
    for right in range(length):
        
        if s[right] not in charMap or charMap[s[right]] < left:
            charMap[s[right]] = right
            maxLength = max(maxLength, right-left+1)
        else:
            left = charMap[s[right]] + 1
            charMap[s[right]] = right
        
    return maxLength

# use array to store 128 int to store the index of each char
def longestNoRepeatSubstring5(s: str)->int:
    maxLength = 0
    chars = [-1]*128
    left = 0
    for right, val in enumerate(s):
        if chars[ord(val)] >= left:
            left = chars[ord(val)]+1
        else:
            maxLength = max(maxLength, right-left+1)
        chars[ord(val)] = right
    return maxLength

testCases = ["abcabcbb", "pwwkew", "au"]
print([longestNoRepeatSubstring(i)  for i in testCases])

print([longestNoRepeatSubstring2(i)  for i in testCases])

print([longestNoRepeatSubstring3(i)  for i in testCases])

print([longestNoRepeatSubstring4(i)  for i in testCases])

print([longestNoRepeatSubstring5(i)  for i in testCases])






"""

Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104


solution:
slide window:

sum(left,right ) >= 7
[2,3,1,2,4,3]
[4,3]

must use the sum calculation, not use pre-defined 

"""
def minLengthOfSubstring(target: int, nums: list[int]) ->int:
    length = len(nums)
    minLength = length + 1
    sum = 0
    left = 0
    for right, num in enumerate(nums):
        sum += num
        while sum>=target:
            # print("hhhhhhh",nums, nums[left:right+1])
            minLength = min(minLength, right-left+1)
            sum -= nums[left]
            left += 1

    if minLength == length + 1:
        return 0
    return minLength



testCases= [[7, [2,3,1,2,4,3]], [4, [1,4,4]], [11, [1,1,1,1,1,1,1,1]]]
print( [minLengthOfSubstring(testCase[0], testCase[1]) for testCase in testCases])


