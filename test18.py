"""

https://leetcode.com/problems/spiral-matrix/solutions/?envType=study-plan-v2&envId=top-interview-150

54. Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.

Given an m x n matrix, return all elements of the matrix in spiral order.


solution: brute force

1, add the exception
2, add direction 'left', 'right', 'up', 'down'


this question need time to conquer
"""

def sprialMarix(matrix: list[list[int]])->list[int]:
    res =[]
    
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)
    
    while left<right and top<bottom:
        
        # from left to right
        for i in range(left, right):
            res.append(matrix[top][i])
        top += 1
        
        # read the right col
        for i in range(top, bottom):
            res.append(matrix[i][right-1])
        right -= 1
        
        # check
        # if not (left<right and top<bottom):
        #     break
        
        # read the bootom
        for i in range(right-1, left-1, -1):
            res.append(matrix[bottom-1][i])
        bottom -= 1
        
        # read the left col
        for i in range(bottom-1, top-1, -1):
            res.append(matrix[i][left])
        left += 1
    
    return res

test_cases = [[[1,2,3],[4,5,6],[7,8,9]]]

print([sprialMarix(test) for test in test_cases])
        
        