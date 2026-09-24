# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverseList(node):
            curr = node
            prev = None
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev

        slow , fast = head, head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        
        tail = slow.next 
        slow.next = None
        tail = reverseList(tail)
        # second = tail

        # while second!= None:
        #     print(second.val)
        #     second = second.next

        while tail :
            temp = head.next
            head.next = tail
            tail = tail.next
            head = head.next
            head.next = temp
            head = head.next
        
        # head.next = tail

        