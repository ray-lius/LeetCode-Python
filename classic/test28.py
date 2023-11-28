"""
104. Maximum Depth of Binary Tree #

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

return its depth = 3.


"""

from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: Optional[TreeNode])->int:
    if root == None:
        return 0
    else:
        return max(maxDepth(root.left), maxDepth(root.right))+ 1




"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if (p == None and q != None) or (p != None and q == None):
            return False
        
        if p == None and q == None :
            return True
        
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False




"""
105. Construct Binary Tree from Preorder and Inorder Traversal

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

example 1:

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]

"""


# solution 1
# rebuild with the tree with the recusive way

def build(preorder: list[int], inorder: list[int])->Optional[TreeNode]:
    if len(preorder) == 0:
        return None
    
    root = TreeNode(preorder[0])
    for idx, num in enumerate(inorder):
        if num == root.val:
            root.left = build(preorder[1:idx+1], inorder[:idx])
            root.right = build(preorder[idx+1:], inorder[idx+1:])
    return root


###############################################################

# BFS get the tree ?????????????????????????
#?????????????????
def build2(preorder: list[int], inorder: list[int])->Optional[TreeNode]:
    inPos = defaultdict(0)
    for idx, num in enumerate(inorder):
        inPos[num] = idx
    
    return build_pre_in_2_tree_DFS(preorder, 0, len(preorder)-1, 0, inPos)


def build_pre_in_2_tree_DFS(preorder: list[int], pre_start: int, pre_end: int, in_start: int, inPos: dict )->Optional[TreeNode]:

    if pre_start>pre_end:
        return None

    root = TreeNode(preorder[pre_start])
    rootIdx = inPos[preorder[pre_start]]
    leftLen = rootIdx - in_start
    root.left = build_pre_in_2_tree_DFS(preorder, pre_start+1, pre_start+leftLen, in_start, inPos)
    root.right = build_pre_in_2_tree_DFS(preorder, pre_start+leftLen+1, pre_end, in_start, inPos)

    return root




"""
106. Construct Binary Tree from Inorder and Postorder Traversal

Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

 

Example 1:

Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]


"""

def build3(inorder:list[int],  postorder:list[int])->Optional[TreeNode]:
    if len(inorder) == 0:
        return None
    
    root = TreeNode(postorder[-1])
    for idx, node in enumerate(inorder):

        if node == postorder[-1]:
            root.left = build3(inorder[:idx], postorder[:idx])
            root.right= build3(inorder[idx+1:], postorder[idx:-1])
    return root



## need resarch
# this way is beautiful!!!!!
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        inorder_map={val:idx for idx, val in enumerate(inorder)}
        postorder_idx=len(postorder)-1

        # what the left and right mean?
        # left: 
        # right: 
        def treeHelper(left, right):
            nonlocal postorder_idx
            if left>right:
                return None

            node_val = postorder[postorder_idx]
            postorder_idx-=1

            inorder_index=inorder_map[node_val]

            root=TreeNode(node_val)
            root.right = treeHelper(inorder_index+1, right)
            root.left = treeHelper(left, inorder_index-1 )
            

            return root

        return treeHelper(0, len(inorder)-1)
    

###################################################
# Divide and conquer ( very important)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution2:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        dic = {}
        for i in range(len(inorder)):
            dic[inorder[i]] = i


        return self.construct(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1, dic)

    def construct(self, ino, in_start, in_end, post, post_start, post_end, dic) -> TreeNode:
        if in_start > in_end or post_start > post_end:
            return None
        
        root = TreeNode(post[post_end])
        ele_left = dic[root.val] - in_start

        root.left = self.construct(ino, in_start, dic[root.val] - 1, post, post_start, post_start + ele_left - 1, dic)
        root.right = self.construct(ino, dic[root.val] + 1, in_end, post, post_start + ele_left, post_end - 1, dic)

        return root




"""
114. Flatten Binary Tree to Linked List

Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

example 1
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [0]
Output: [0]


solution 1: recusive 


root.left.right= root.right
root.right = root.left
root.left = None

"""

def flatten(root: Optional[TreeNode]) -> None:
    if root == None:
        return None
    
    flatten(root.right)
    flatten(root.left)
    
    cur_right =root.right
    root.right= root.left
    root.left = None
    
    while root.right != None:
        root = root.right

    root.right = cur_right
    


##############################
# some basic things:


def printInorder(root:Optional[TreeNode])->None:
    
    if root:
        printInorder(root.left)
        print(root.val, end=" | ")
        printInorder(root.right)


def printPreorder(root:Optional[TreeNode])->None:
    
    if root:
        
        print(root.val, end=" | ")
        printInorder(root.left)
        printInorder(root.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print('\nPrint tree inorder traverse ')
printInorder(root)
print('\nPrint tree preorder traverse')
printPreorder(root)

flatten(root)

print('\nPrint tree inorder traverse ')
printInorder(root)
print('\nPrint tree preorder traverse')
printPreorder(root)
