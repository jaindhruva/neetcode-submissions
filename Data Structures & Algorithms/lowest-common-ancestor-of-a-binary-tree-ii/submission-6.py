# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = []
        order = []

        stack.append(root)

        # fill stack and build order
        while stack:
            node = stack.pop()
            order.append(node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        nodeCount = {}
        for node in reversed(order):
            count = int(node is p or node is q)

            count += nodeCount[node.left] if node.left else 0
            count += nodeCount[node.right] if node.right else 0

            if count == 2:
                return node

            nodeCount[node] = count
        
        return None


            

            
            
                
