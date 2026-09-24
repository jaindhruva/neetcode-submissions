# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        kthsmallest = -1
        def inorder(node, k):
            nonlocal kthsmallest
            if node == None  :
                return k
            
            k = inorder(node.left, k)
            k -= 1
            if k == 0:
                kthsmallest = node.val
                return k
            k = inorder(node.right, k)
            return k
        
        inorder(root, k)
        return kthsmallest