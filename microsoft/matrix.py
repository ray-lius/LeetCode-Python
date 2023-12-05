""" 
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.

"""
from collections import deque


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        
        record = [[-1 for _ in mat[0]] for _ in mat]
        queue = deque()
        print(record)
        
        rows, cols = len(mat), len(mat[0])
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    record[i][j] = 0
                    queue.append((i,j))
        print(record, queue)
        
        directions = [[1,0], [0,1], [-1,0], [0, -1]]
        while queue:
            x,y = queue.popleft()
            for d in directions:
                nx = x+d[0]
                ny = y+d[1]
                if -1 < nx < rows and -1 < ny < cols:
                    if record[nx][ny] <0:
                        record[nx][ny] = record[x][y] + 1
                        queue.append((nx, ny))
        
        return record
    

def test_func():
    solution = Solution()
    print(solution.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
    
    
test_func()
                
            
                    
