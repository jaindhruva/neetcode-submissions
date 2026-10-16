import sys
sys.setrecursionlimit(20000)

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, nodes: List[TreeNode]) -> TreeNode:
        
        lca = None
        target_set = set(nodes)
        target_count = len(nodes)

        def post_order(node):
            nonlocal lca
            count = 0
            if lca is not None or node is None:
                return 0
            
            left_count = post_order(node.left)
            right_count = post_order(node.right)

            if node in target_set:
                count += 1
            
            count += left_count + right_count

            if count == target_count and not lca:
                lca = node
            
            return count

        
        post_order(root)
        return lca
        
