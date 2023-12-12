""" 
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105

"""

class Solution:
    def trap(self, height: list[int]) -> int:
        if len(height) < 3:
            return 0
        stack = []
        res = 0
        for idx, val in enumerate(height):
            
            while stack and val>height[stack[-1]]:
                prev = stack[-1]
                stack.pop()
                if not stack: break
                
                left = stack[-1]
                l = idx - left -1
                h = min(val, height[left]) - height[prev]
                res += l*h
            
            stack.append(idx)
        return res


def trapWater(height: list[int]):
    if len(height) < 3:
        return 0
    stack = []
    res = 0
    for idx, val in enumerate(height):

        while stack and val > height[stack[-1]]:
            base = stack.pop()
            if not stack:
                break
            l = idx - stack[-1] - 1
            h = min(val, height[stack[-1]]) - height[base]
            res += l*h

        stack.append(idx)

    return res

def test_func():

    solution = Solution()
    print(solution.trap([0, 1, 0,2,1,0,1,3,2,1,2,1]))
    print(solution.trap([4, 2, 0, 3, 2, 5]))
    
    print(trapWater([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(trapWater([4, 2, 0, 3, 2, 5]))
    
test_func()
