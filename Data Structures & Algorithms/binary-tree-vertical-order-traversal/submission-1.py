# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        cols = defaultdict(list)
        q = deque() # node , col
        q.append((root, 0))
        minCol = maxCol = 0

        while q:
            node, col = q.popleft()
            minCol = min(col, minCol)
            maxCol = max(col, maxCol)
            cols[col].append(node.val)

            if node.left:
                q.append((node.left, col-1))
            if node.right:
                q.append((node.right, col+1))
            

        res = []
        for c in range(minCol, maxCol+1):
            res.append(cols[c])

        return res
