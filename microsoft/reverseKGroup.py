""" 
25. Reverse Nodes in k-Group

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
Example 1
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def findKthNode(self, curr: Optional[ListNode], k: int) -> Optional[ListNode]:
        while curr and k>0:
            curr = curr.next
            k -= 1
        return curr
        
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 1:
            return head
        
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        curr = head
        while curr:
            tail = self.findKthNode(curr, k-1)
            if not tail:
                break
            next_head = tail.next
            tail.next = None
            prev.next = self.reverse(curr)
            curr.next = next_head
            prev = curr
            curr = next_head
        return dummy.next
    
class Solution2:
    def findKth(self, curr:Optional[ListNode], k: int) ->Optional[ListNode]:
        while curr and k>0:
            curr = curr.next
            k -= 1
        return curr
        
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or not head.next or k==1:
            return head
        
        dummy = ListNode(0, head)
        groupPrev = dummy
        
        while True:
            kth = self.findKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next
            
            # group node reverse
            curr, prev = groupPrev.next, kth.next
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
            
        return dummy.next
        

def printListNode(head: ListNode):
    stack = []
    cur = head
    while cur:
        stack.append(cur.val)
        cur = cur.next
    print(stack)
        

def test_func():
    head = ListNode(1, None)
    head.next = ListNode(2, None)
    head.next.next = ListNode(3, None)
    head.next.next.next = ListNode(4, None)
    head.next.next.next.next = ListNode(5, None)
    
    printListNode(head)
    solution = Solution()
    result = solution.reverseKGroup(head, 2)
    printListNode(result)
    
    #  reverse back
    solution2 = Solution2()
    result2 = solution2.reverseKGroup(result, 2)
    printListNode(result2)
    
    
test_func()
    
