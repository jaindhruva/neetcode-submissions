# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        q.append(root)
        res = []

        while q:
            size = len(q)
            last_node = None
            for i in range(size):
                node = q.popleft()
                if not node:
                    continue
                last_node = node
                q.append(node.left)
                q.append(node.right)
            if last_node:
                res.append(last_node.val)
        return res
