"""

150. Evaluate Reverse Polish Notation
Medium
6.5K
949
Companies
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22


solution 1:
just follow the calculation, get the result dn replace the orginal place


"""

import operator


def evalRPN( tokens: list[str]) -> int:

    index = 2
    symbols = ['+', '-', '*','/' ]
    while index < len(tokens):
        print (index, tokens)
        if tokens[index] in symbols:
            if tokens[index] == '+':
                res = int(tokens[index-2]) + int(tokens[index-1])
            if tokens[index] == '-':
                res = int(tokens[index-2]) - int(tokens[index-1])
            if tokens[index] == '*':
                res = int(tokens[index-2]) * int(tokens[index-1])
            if tokens[index] == '/':
                res = int(int(tokens[index-2]) / int(tokens[index-1]))
                
            tokens[index-2] = str(res)
            tmp = index - 2
            tokens.pop(index)
            tokens.pop(index-1)
            index = tmp
        else:
            index += 1
        
    return tokens[-1]


def evalRPN2( tokens: list[str]) -> int:
    operators = {
        '+': (lambda x, y: x + y),
        '-': (lambda x, y: x + y),
        '*': (lambda x, y: x * y),
        '/': (lambda x, y: int(x/y))
    }

    stack = []
    for token in tokens:
        if token not in operators:
            stack.append(int(token))
        else:
            x = stack.pop(-2)
            y = stack.pop()
            stack.append(operators[token](x, y))
    return stack[-1]






    return 0



test_cases = [["2","1","+","3","*"], ["10","6","9","3","+","-11","*","/","*","17","+","5","+"], ["4","-2","/","2","-3","-","-"]]
print([evalRPN(i) for i in test_cases])

print([evalRPN2(i) for i in test_cases])




queue = [(2, 1)]
root, num = queue.pop(0)
print(root, num)


print(operator.add(1, 3))
print('3'+'2')
