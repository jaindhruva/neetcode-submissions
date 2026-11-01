# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = {}

        def postOrder(node):
            if not node:
                return -1
            
            leftHeight = postOrder(node.left)
            rightHeight = postOrder(node.right)
            currHeight = max(leftHeight, rightHeight) + 1

            if currHeight not in res:
                res[currHeight] = []
            res[currHeight].append(node.val)

            return currHeight

        postOrder(root)

        return list(res.values())


