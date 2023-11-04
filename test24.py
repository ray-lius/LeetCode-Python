"""
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.


"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    head = ListNode(0)
    n1 = n2 = 0
    carry = 0
    current = head
    while l1 != None or l2 != None or carry != 0:
        if l1 == None:
            n1 = 0
        else:
            n1 = l1.val
            l1 = l1.next
        
        if l2 == None:
            n2 = 0
        else:
            n2 = l2.val
            l2 = l2.next
        
        current.next = ListNode((n1 + n2 + carry) % 10)
        current = current.next
        carry = (n1 + n2 + carry) // 10

    return head.next


def printNode(n: Optional[ListNode])->None:
    res = []
    while n:
        res.append(str(n.val))
        n = n.next
    print("->".join(res)) 


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

printNode(l1)
printNode(l2)

l3 = addTwoNumbers(l1, l2)

printNode(l3)

"""
21. Merge Two Sorted Lists

Companies
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.


example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


"""

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode])->Optional[ListNode]:
    if list1 == None:
        return list2
    if list2 == None:
        return list1
    
    if list1.val > list2.val:
        list2.next = mergeTwoLists(list2.next, list1)
        return list2
    
    list1.next = mergeTwoLists(list1.next, list2)
    return list1




l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

printNode(l1)
printNode(l2)

l3 = mergeTwoLists(l1, l2)

printNode(l3)


list0 = [ [] for _ in range(3)]
for i in range(3):
    list0[i] = [False for _ in range(5)]
print (list0)



"""

148 sort list
Given the head of a linked list, return the list after sorting it in ascending order.

example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []

这道题只能用归并排序才能符合要求。归并排序需要的 2 个操作在其他题目已经出现过了，取中间点是第 876 题，合并 2 个有序链表是第 21 题。

################# hard!!!!!!!################

"""


def sortList(head: ListNode)->ListNode:
    pass



"""
EASY but important 

206. Reverse Linked List #
题目 #
Reverse a singly linked list.

题目大意 #
翻转单链表

解题思路 #
按照题意做即可。


use a listnode: behind to catch each node, from head to tail

"""

def reverseList (head: ListNode)->ListNode:
    behind = ListNode()

    while head != None:
        next = head.next
        head.next = behind
        behind = head
        head = next
    
    return behind