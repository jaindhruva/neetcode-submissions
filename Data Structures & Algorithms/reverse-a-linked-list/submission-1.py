# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = None
        next = head
        while (next != None):
            prev = current
            current = next
            next = current.next
            current.next = prev
        
        return current
