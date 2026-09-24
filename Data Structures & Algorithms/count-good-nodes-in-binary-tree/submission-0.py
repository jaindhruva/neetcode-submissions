# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def preorder(node, max_so_far):
            count = 0
            if not node:
                return 0
            if node.val >= max_so_far :
                max_so_far = node.val
                count += 1
            count += preorder(node.left, max_so_far)
            count += preorder(node.right, max_so_far)
            return count
        
        max_so_far = -101
        return preorder(root, max_so_far)