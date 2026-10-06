# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        for head in lists:
            while head:
                heapq.heappush(minHeap, head.val)
                head = head.next
        
        dummy = ListNode(-1)
        node = dummy
        while minHeap:
            node.next = ListNode(heapq.heappop(minHeap))
            node = node.next
        
        return dummy.next
