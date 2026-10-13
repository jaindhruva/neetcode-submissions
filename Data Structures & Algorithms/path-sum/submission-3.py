# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:


        def preorder(node, pathSum):
            if node == None:
                return False
            
            pathSum += node.val
            if not node.left and not node.right:
                if pathSum == targetSum:
                    return True
                return False
            left = preorder(node.left, pathSum)
            right = preorder(node.right, pathSum)

            return left or right
        
        return preorder(root, 0)