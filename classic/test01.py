"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


"""

def isValid(s: str) -> bool:
    leftBracket= ["(", "[", "{"]
    stack = []
    for idx, val in enumerate(s):
        print(idx, val)
        if(val in leftBracket):
            stack.append(val)
        elif (val == ')' and len(stack) > 0 and stack[-1]=='(') or (val == ']' and len(stack) > 0 and stack[-1]=='[') or ((val == '}' and len(stack) > 0 and stack[-1]=='{')):
            stack.pop()
        else:
            return False
    return len(stack) == 0





testString = "()[]{"
print(isValid(testString))



"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

 

Example 1:

Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.
Example 2:

Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 3:

Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= num <= 3999
"""
"""
Solution1: 
1, list all map values and symblos, 1->I
2, compare each 


"""
def intToRoman(num: int) -> str:
    result = ''
    values  = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ["M","CM", "D", "CD", "C","XC", "L", "XL", "X","IX", "V", "IV", "I"]
    idx = 0
    # O(n) = n*len(values) + n
    while num != 0:
        while values[idx]>num:
            idx += 1
        num -= values[idx]
        result += symbols[idx]
    
    return result
    


testList = [4, 9, 58, 1994]

print( [intToRoman(i) for i in testList ])
# result should be: LXXX