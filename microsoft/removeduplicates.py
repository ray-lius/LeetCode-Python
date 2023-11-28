""" 
 1209. Remove All Adjacent Duplicates in String II


You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

 

Example 1:

Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.
Example 2:

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"
Example 3:

Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"
 

Constraints:

1 <= s.length <= 105
2 <= k <= 104




bruteforce, check if has k sub, if have => go delete  and then check again

scrifice some space complexity , build stack to store the data
[ [] , [] , [] ]
"""


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        
        # def delete_diplicate(sub: str)->bool:
        #     start, end  = 0, 0
        #     res = ""
        #     for i in range(1, len(sub)):
        #         count = 0
        #         if sub[i] == sub[i-1]:
        #             count += 1
        #             end += 1
        #         else:
        #             count = 0
        #             start = i
        #             end = i
        #         if count >= k:
        #             res = sub[:start] + sub[end:]
        #     return res
            
        # def backtracking()->None:
        #     pass
            
        # return s
        
        # [char, count]
        stack = [] 
        
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
            else:
                stack.append([char, 1])
            
            if stack[-1][1] == k:
                stack.pop()
        
        res = ""
        for char, count in stack:
            res += (char * count)
        
        return res
    
    
def test_func():
    solution = Solution()
    print(solution.removeDuplicates("deeedbbcccbdaa", 3))
    print(solution.removeDuplicates("pbbcggttciiippooaais",2))
    
    
    test_arr = [1,1,1, 2,2,2, 3,3]
    test_set = set(test_arr)
    print (test_set)
    test_set.add(1)
    print(test_set)
    
test_func()
