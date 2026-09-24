# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_dia = 0

        def postorder(node):
            nonlocal max_dia 
            if not node:
                return 0
            left = postorder(node.left)
            right = postorder(node.right)
            max_dia = max(max_dia,left+right)
            return 1+max(left,right)
        
        postorder(root)
        return max_dia
        