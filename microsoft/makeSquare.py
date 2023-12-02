""" 

You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.

 

Example 1:


Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
Example 2:

Input: matchsticks = [3,3,3,3,4]
Output: false
Explanation: You cannot find a way to form a square with all the matchsticks.
 

Constraints:

1 <= matchsticks.length <= 15
1 <= matchsticks[i] <= 108



dp
"""

class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
    
        side = sum(matchsticks)//4
        if sum(matchsticks)/4 != side:
            return False
        sides = [0] * 4
        
        # decending order as we need to check if teh max over the design value
        matchsticks.sort(reverse=True)
        
        def backtracking(idx: int) -> bool:
            if idx == len(matchsticks):
                return True
            
            for i in range(4):
                if sides[i]+matchsticks[idx] <= side:
                    sides[i] += matchsticks[idx]
                    if backtracking(idx+1):
                        return True
                    sides[i] -= matchsticks[idx]
            return False
    
        return backtracking(0)
    
    
    
def test():
    matches = [1,1,2,2,2]
    solution = Solution()
    print(solution.makesquare(matches))
    
test()