"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000



P   A   H   N
A P L S I I G
Y   I   R

      n*2
0     6    12
P     I    N
A   L S  I G
Y A   H R
P     I



set a Matrix
[a, ,c, ,d]
[a, ]
and set a up and down to control the direction

"""


# use matrix = [[] for _ in range(numRows)]  to build the matrix format
# don't use the matrix [[]] & numRows, they are different

def zigZagConvert(s:str, numRows:int)->str:
    matrix = [[] for _ in range(numRows)]
    up = numRows-2
    down = 0
    idx =0 
    while idx < len(s):
        if down < numRows:
            matrix[down].append(s[idx])
            down += 1
            idx += 1
        elif up >0:
            matrix[up].append(s[idx])
            up -= 1
            idx += 1
        else:
            up = numRows-2
            down = 0
        
    result = ""
    for i in matrix:
        result += "".join(i)
    
    return result

testCases = [["PAYPALISHIRING", 3],["PAYPALISHIRING", 4]]
print([zigZagConvert(i[0], i[1]) for i in testCases])

