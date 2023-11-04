""" 
medium question 01
Longest palindromic substring


res
dp = []

s[i] == s[j] && (j-i<3 or dp[i+1][j-1]) 
dp[i][j] = True


"""

def longestPalindromicSubstring(s: str)->str:
    res = ""
    s_len = len(s)
    dp = [ [ False for _ in range(s_len)] for _ in range(s_len)]
    
    for i in range(s_len-1):
        for j in range(i+1, s_len):
            if s[i]==s[j] and (j-i<3 or dp[i+1][j-1]):
                dp[i][j] = True
            if dp[i][j] == True and (res == "" or j-i+1 > len(res)):
                res = s[i:j+1]
    return res
    
    
test_cases = ["babad", "cbbd"]
print([longestPalindromicSubstring(test) for test in test_cases])


""" 

climb stairs

how many ways to get to n stairs, each time can climb 1-2 stairs

solution1:
dp[i] = dp[i-1] + dp[i-2]
"""

def climbStairs(n: int)->int:
    
    dp = [ -1 for _ in range(n+1)]
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

test_cases_2 = [2, 3, 9]
print([climbStairs(test) for test in test_cases_2])