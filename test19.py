"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.



solution 1:

brute force

solution2:

solution reversed first, then swap agnostically


solution 3:


"""


def rotate(matrix: list[list[int]])-> None:
    length = len(matrix)
    rotataMatrix = [[0 for _ in range(length)] for _ in range(length)]


    for row_idx, row in enumerate(matrix):
        for idx, val in enumerate(row):
            rotataMatrix[idx][length-1-row_idx] = val
            
    
    return rotataMatrix


def rotate2(matrix: list[list[int]])-> None:
    matrix = list(reversed(matrix))
    n = len(matrix)

    for i in range(n):
        for j in range(i+1, n):
            tmp = matrix[j][i]
            matrix[j][i] = matrix[i][j]
            matrix[i][j] = tmp
            
    
    return matrix

def rotate3(matrix: list[list[int]])-> None:
    
    n = len(matrix)

    for i in range(n//2):
        for j in range(n):
            tmp = matrix[n-i-1][j]
            matrix[n-i-1][j] = matrix[i][j]
            matrix[i][j] = tmp

    for i in range(n):
        for j in range(i+1, n):
            tmp = matrix[j][i]
            matrix[j][i] = matrix[i][j]
            matrix[i][j] = tmp
            
    
    return matrix



testCases = [[[1,2,3],[4,5,6],[7,8,9]], [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]]
testCases2 = [[[1,2,3],[4,5,6],[7,8,9]], [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]]
testCases3 = [[[1,2,3],[4,5,6],[7,8,9]], [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]]

print([rotate(i) for i in testCases])

print([rotate2(i) for i in testCases2])
print([rotate3(i) for i in testCases3])
