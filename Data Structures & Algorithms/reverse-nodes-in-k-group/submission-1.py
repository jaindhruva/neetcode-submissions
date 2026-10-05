# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def getKthNode(node):
            count = 0
            while node and count<k:
                node = node.next
                count += 1
            return node 

        dummy = ListNode(-1)
        dummy.next = head
        groupPrev = dummy
        
        while True:
            
            kthNode = getKthNode(groupPrev)
            # print(kthNode)
            if not kthNode:
                break
            groupNext = kthNode.next

            prev, curr = kthNode.next, groupPrev.next
            while curr != groupNext:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            
            tmp = groupPrev.next
            groupPrev.next = kthNode
            groupPrev = tmp

        return dummy.next
        
        


        