""" 

multiple DP ---------------------_____======================

120 Triangle

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
Example 2:

Input: triangle = [[-10]]
Output: -10
 

Constraints:

1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-104 <= triangle[i][j] <= 104


"""

# O(n), no extra space
import sys


def minimumTotal(triangle: list[list[int]]) -> int:
    if len(triangle) == 0:
        return 0
    if len(triangle) == 1:
        return triangle[0][0]
    
    length = len(triangle)
    for col in range(length-2, -1, -1):
        col_len = len(triangle[col])
        for row in range(col_len):
            triangle[col][row] += min(triangle[col+1][row], triangle[col+1][row+1])
    return triangle[0][0]



# space: O(n)
def minimumTotal1(triangle: list[list[int]]) -> int:
    len_triangle = len(triangle)
    if len_triangle == 0:
        return [[]]
    
    dp = [0 for _ in triangle[-1]]
    for idx, each in enumerate(triangle[0]):
        dp[idx] = each
    for col in range(1, len_triangle):
        col_len = len(triangle[col])
        for row in range(col_len-1, -1, -1):
            if row == 0:
                dp[row] += triangle[col][0]
            elif row == col_len-1:
                dp[row] += dp[row-1] + triangle[col][row]
            else:
                dp[row] =  min(triangle[col][row] + dp[row-1], triangle[col][row]+ dp[row])
     
    # print (dp)
    return min(dp)
    


test_cases = [[[2],[3,4],[6,5,7],[4,1,8,3]]]
print([minimumTotal(test) for test in test_cases])

test_cases_2 = [[[2],[3,4],[6,5,7],[4,1,8,3]]]
print([minimumTotal1(test) for test in test_cases_2])


""" 
64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.


Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12


solution :
dp
dp[i][j] = min (dp[i-1][j], dp[i][j-1])
until 
m = i, n = j


"""

def minPathSum(grid: list[list[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    
    # dp = []
    # for i in range(m):
    #     row = []
    #     for j in range(n):
    #         row.append(0)
    #     dp.append(row)

    for col in range(m):
        for row in range(n):
            if col == 0 and row == 0:
                continue
            
            if col == 0:
                grid[col][row] += grid[col][row-1]
            elif row == 0:
                grid[col][row] += grid[col-1][row]
            else:
                grid[col][row] = min(grid[col][row] + grid[col-1][row], grid[col][row] + grid[col][row-1])
    print(grid)
    return grid[-1][-1]




test_cases_3 = [[[1,3,1],[1,5,1],[4,2,1]]]

print([minPathSum(test) for test in test_cases_3])


""" 

63. Unique Paths II
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.

example 1:
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right


example 2:
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1


"""

def uniquePathsWithObstacles(obstacleGrid: list[list[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[ 0 for _ in range(n)] for _ in range(m)]
    
    
        for col in range(m):
            for row in range(n):
            
                if obstacleGrid[col][row] == 1:
                    dp[col][row] = 0
                elif col == 0 and row == 0:
                    dp[col][row] = 1
                elif col == 0:
                    dp[col][row] = dp[col][row-1]
                elif row == 0:
                    dp[col][row] = dp[col-1][row]
                else:
                
                    if obstacleGrid[col][row-1] == 1:
                        dp[col][row] = dp[col-1][row]
                    elif obstacleGrid[col-1][row] == 1:
                        dp[col][row] = dp[col][row-1]
                    else:
                        dp[col][row] = dp[col][row-1] + dp[col-1][row]
        return dp[-1][-1]


test_cases_4 = [[[0,0,0],[0,1,0],[0,0,0]], [[0,1],[0,0]], [[0,0],[0,1]]]

print([uniquePathsWithObstacles(test) for test in test_cases_4])




""" 
5. Longest Palindromic Substring #

Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

Example 3:

Input: s = "a"
Output: "a"

Example 4:

Input: s = "ac"
Output: "a"

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),


solution 3:
1) brutal force
get every comb, an cal isPalindromic str

return s == s[::-1]

2) DP 
dp = [bool]
s[i] -> s[j]
dp[i][j] = s[i]==s[j] and (j-i<3 or dp[i+1][j-1])
 
 
"""

# O(n^2)
def isPalindrome(s:str)->bool:
    return s == s[::-1]

def longestPalindrome(s: str) -> str:
    
    maxPaLen = 0
    res = ''
    s_len  = len(s)
    for i in range(s_len):
        for j in range(i+1, s_len+ 1):
            if isPalindrome(s[i:j]) and j-i>maxPaLen:
                
                maxPaLen = j-i
                res = s[i:j]
                
    return res
    
# O(n^2)
# ######## must be reverse to read the i in the range of s
def longestPalindrome2(s: str) -> str:
    
    res = ""
    s_len  = len(s)
    
    dp =[[ False for _ in range(s_len)] for _ in range(s_len)]
    
    for i in range(s_len-1, -1, -1):
        for j in range(i, s_len):
            dp[i][j] = s[i]==s[j] and (j-i<=3 or dp[i+1][j-1]) 
            if dp[i][j] and (res=="" or j-i+1>len(res)):
                res = s[i:j+1]
                
    return res
    

# centra

# O(n)
# manaker algorithm
def longestPalindrome3(s: str) -> str:
    
    pass



test_cases_5= ["babad", "cbbd", "aaaaa"]
print(' Longest Palindromic Substring', [longestPalindrome(test) for test in test_cases_5])
print(' Longest Palindromic Substring', [longestPalindrome2(test) for test in test_cases_5])

if []:
    print("oooo")
else:
    print("llllll")
    
print([1]+[2,3,4])