""" 
206. Reverse Linked List
 
Given the head of a singly linked list, reverse the list, and return the reversed list.


"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            third = cur.next
            
            #  reverse the lined list here
            cur.next = prev
            prev = cur
            
            cur = third
        return prev