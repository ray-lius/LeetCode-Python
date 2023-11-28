""" 
1239 max length
You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
Explanation: The only string in arr has all 26 characters.

"""

from collections import Counter


class Solution:
    
    def checkUnique(self, string: str) -> bool:
        char_arr = []
        for each in string:
            if each not in char_arr:
                char_arr.append(each)
            else:
                return False
        return True
    
    def maxLength(self, arr: list[str]) -> int:
        
        def backtracking(arr, idx, substring)->int:
            if idx == len(arr):
                return len(substring)
            else:
                if self.checkUnique(substring+arr[idx]):
                    return max(backtracking(arr, idx+1, substring), backtracking(arr, idx+1, substring+arr[idx]))
                else:
                    return backtracking(arr, idx+1, substring)
        
        return backtracking(arr, 0, "")
    
    
def test_func():
    solution = Solution()
    
    print(solution.maxLength(["un", "iq", "ue"]))
    print(solution.maxLength(["cha", "r", "act", "ers"]))
    print(solution.maxLength(["abcdefghijklmnopqrstuvwxyz"]))
    
    print(Counter("abcdefghijklmnopqrstuvwxyz"))
    print(Counter("abcdefghijklmnopqrstuvwxyz").keys())
    print(Counter("abcdefghijklmnopqrstuvwxyz").values())
    


test_func()
        