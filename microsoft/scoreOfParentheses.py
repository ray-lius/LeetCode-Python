""" 
856. Score of Parentheses

Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
 

Example 1:

Input: s = "()"
Output: 1
Example 2:

Input: s = "(())"
Output: 2
Example 3:

Input: s = "()()"
Output: 2
 

Constraints:

2 <= s.length <= 50
s consists of only '(' and ')'.
s is a balanced parentheses string.




((()()))(())

stack = [8]

score 2, 4, 8, 0, 1
"""

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # score = 0
        # # count of left (
        # sub_score = 0
        # stack = []
        
        # for char in s:
        #     if sub_score == 0 and char == "(":
        #         sub_score += 1
        #         stack.append('(')
        #     elif char == "(":
        #         sub_score *= 2
        #         stack.append('(')
        #     else:
        #         stack.pop()
            
        #     if not stack:
                
        #         score += sub_score
        #         sub_score = 0
                
        # return score
        
        score = 0
        stack = []
        
        for char in s:
            if char == "(":
                stack.append(score)
                score = 0
            else:
                score = stack.pop() + max(score*2, 1)
        return score
    def scoreOfParentheses2(self, s: str) -> int:
        
        score, mul = 0, 0
        
        for idx, char in enumerate(s):
            if char == '(':
                mul += 1
            else:
                mul -= 1
                if idx > 0 and s[idx-1] == "(":
                    score += 2**mul
        return score

def test_func():
    solution = Solution()
    print(solution.scoreOfParentheses("(())((()()()))()"))
    print(solution.scoreOfParentheses("()()"))
    
    print(solution.scoreOfParentheses2("(())((()()()))()"))
    print(solution.scoreOfParentheses2("()()"))
    
    str = "abc"
    print(str * 8)



test_func()
