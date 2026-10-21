# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        lca = None

        def postOrder(node):
            nonlocal lca
            if (not node) or lca:
                return False
            left = postOrder(node.left)
            right = postOrder(node.right)
            
            center = False
            if node.val == p.val or node.val == q.val:
                center = True
            
            if (left and right) or (center and (left or right)) :
                if not lca:
                    lca = node

            return left or right or center
        
        postOrder(root)
        return lca

#            5
#       3         4
#    2     1


                