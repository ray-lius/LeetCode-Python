"""
https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/description/
You are given a 0-indexed 2D integer matrix grid of size 3 * 3, representing the number of stones in each cell. The grid contains exactly 9 stones, and there can be multiple stones in a single cell.

In one move, you can move a single stone from its current cell to any other cell if the two cells share a side.

Return the minimum number of moves required to place one stone in each cell.

 

Example 1:


Input: grid = [
    [1,1,0],
    [1,1,1],
    [1,2,1]
    ]
Output: 3
Explanation: One possible sequence of moves to place one stone in each cell is: 
1- Move one stone from cell (2,1) to cell (2,2).
2- Move one stone from cell (2,2) to cell (1,2).
3- Move one stone from cell (1,2) to cell (0,2).
In total, it takes 3 moves to place one stone in each cell of the grid.
It can be shown that 3 is the minimum number of moves required to place one stone in each cell.
Example 2:


Input: grid = [
    [1,3,0],
    [1,0,0],
    [1,0,3]
    ]
Output: 4
Explanation: One possible sequence of moves to place one stone in each cell is:
1- Move one stone from cell (0,1) to cell (0,2).
2- Move one stone from cell (0,1) to cell (1,1).
3- Move one stone from cell (2,2) to cell (1,2).
4- Move one stone from cell (2,2) to cell (2,1).
In total, it takes 4 moves to place one stone in each cell of the grid.
It can be shown that 4 is the minimum number of moves required to place one stone in each cell.
 

Constraints:

grid.length == grid[i].length == 3
0 <= grid[i][j] <= 9
Sum of grid is equal to 9.




Tim conplexity:
1, 8 = 8
2, 7 = 7^2
3, 6 = 

empty = n

"""



import sys
class Solution:
    def __init__(self) -> None:
        self.min = sys.maxsize
        
    def minimumMoves(self, grid: list[list[int]]) -> int:
        self.dfs(0, 0, grid)
        return self.min
        
    def dfs(self, pos: int, moves: int, grid: list[list[int]]) -> None:
        
        if moves >= self.min:
            return 
        
        if pos == 9:
            self.min = min(self.min, moves)
            return
        
        pos_x = pos//3
        pos_y = pos%3
        
        if grid[pos_x][pos_y] != 0:
            self.dfs(pos+1, moves, grid)
            return
        
        for j in range(3):
                for k in range(3):
                    if grid[j][k] > 1:
                        grid[j][k] = grid[j][k] - 1
                        grid[pos_x][pos_y] = grid[pos_x][pos_y] + 1
                        self.dfs(pos+1, moves+abs(j-pos_x) + abs(k-pos_y), grid)
                        grid[j][k] = grid[j][k] + 1
                        grid[pos_x][pos_y] = grid[pos_x][pos_y] - 1
                        

def test():
    testcase = [
        [1, 1, 0],
        [1, 1, 1],
        [1, 2, 1]
     ]
    testcase2 = [
        [1, 3, 0],
        [1, 0, 0],
        [1, 0, 3]
    ]
    solution = Solution()
    print(solution.minimumMoves(testcase))
    solution2 = Solution()
    print(solution2.minimumMoves(testcase2))


test()