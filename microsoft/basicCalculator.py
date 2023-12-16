""" 
224. Basic Calculator

Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
 

Constraints:

1 <= s.length <= 3 * 105
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
'-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.


"""

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res, preSign, num = 0, 1, 0
        for char in s:
            if char>='0' and char<='9':
                num = num*10 + (ord(char)-ord('0'))
            elif char == "+":
                res += preSign * num
                preSign, num = 1, 0
            elif char == "-":
                res += preSign * num
                preSign, num = -1, 0
            elif char == "(":
                stack.append(res)
                stack.append(preSign)
                res, preSign = 0, 1
            elif char == ")":
                res += preSign * num
                num = 0
                res *= stack.pop()
                res += stack.pop()
        return res + preSign*num
    

def basicCalcu(s: str) -> int:
    stack = []
    sign, num, res = 1, 0, 0

    for char in s:
        if char >= '0' and char <= '9':
            num = num*10 + (ord(char)-ord('0'))
        elif char == '-':
            res += sign*num
            num, sign = 0, -1
        elif char == '+':
            res += sign*num
            num, sign = 0, 1
        elif char == '(':
            stack.append(res)
            stack.append(sign)
            res, sign = 0, 1
        elif char == ')':
            res += sign*num
            res *= stack.pop()
            res += stack.pop()
            num = 0
    return res + sign*num



def test_func():
    solution = Solution()
    s_1 = "(1+(4+5+2)-3)+(6+8)" #23
    print(solution.calculate(s_1))
    print(basicCalcu(s_1))
    s_2 = "9+(1+(4+5+2)-3)+(6+8)-8" #24
    print(solution.calculate(s_2))
    print(basicCalcu(s_2))
    s_3 = "10-((1+(4+5+2)-3)+(6+8))+9" #-4
    print(solution.calculate(s_3))
    print(basicCalcu(s_3))
    
test_func()


