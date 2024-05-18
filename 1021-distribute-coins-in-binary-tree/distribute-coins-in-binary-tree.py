# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            left_excess = dfs(node.left)
            right_excess = dfs(node.right)
            total_moves[0] += abs(left_excess) + abs(right_excess)
            return node.val + left_excess + right_excess - 1

        total_moves = [0]
        dfs(root)
        return total_moves[0]