""" 
951. Flip Equivalent Binary Trees

For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivalent or false otherwise.


Example 1:

Flipped Trees Diagram
Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true
Explanation: We flipped at nodes with values 1, 3, and 5.
Example 2:

Input: root1 = [], root2 = []
Output: true
Example 3:

Input: root1 = [], root2 = [1]
Output: false

Constraints:

The number of nodes in each tree is in the range [0, 100].
Each tree will have unique node values in the range [0, 99].

"""


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 or not root2:
            return not root1 and not root2
        
        if root1.val != root2.val:
            return False
        
        return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))
    
    
def test_func():
    node1_7 = TreeNode(7)
    node1_8 = TreeNode(8)
    node1_5 = TreeNode(5, node1_7, node1_8)
    node1_4 = TreeNode(4)
    node1_2 = TreeNode(2, node1_4, node1_5)
    node1_6 = TreeNode(6)
    node1_3 = TreeNode(3, node1_6)
    node1_1 = TreeNode(1, node1_2, node1_3)
    
    node2_7 = TreeNode(7)
    node2_8 = TreeNode(8)
    node2_5 = TreeNode(5, node2_8, node2_7)
    node2_4 = TreeNode(4)
    node2_2 = TreeNode(2, node2_4, node2_5)
    node2_6 = TreeNode(6)
    node2_3 = TreeNode(3, None ,node2_6)
    node2_1 = TreeNode(1, node2_3, node2_2)
    
    solution = Solution()
    print(solution.flipEquiv(node1_1, node2_1))
    
    print(solution.flipEquiv(TreeNode(0), TreeNode(0)))
    print(solution.flipEquiv(TreeNode(0), None))
test_func()
