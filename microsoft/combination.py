""" 
77. Combinations

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.


"""

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        
        comb = []
        
        def backtracking(idx: int, container: list[int])->None:
            if idx == n+1:
                return 
            
            if len(container) == k:
                comb.append(container[:])
                return 
            else:
                container.append(idx+1)
                backtracking(idx+1, container)
                container.remove(idx+1)
                backtracking(idx+1, container)
        
        
        backtracking(0,[])
        
        return comb
    
    
def test_func():
    solution = Solution()
    print(solution.combine(4, 2))
    print(solution.combine(1, 1))
    
test_func()