# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float("-inf")

        def postorder(node):
            nonlocal maxSum
            if not node:
                return 0
            left = max(0, postorder(node.left))
            right = max(0, postorder(node.right))
            maxSum = max(maxSum, left+right+node.val)
            return max(left,right) + node.val
        
        postorder(root)
        return maxSum