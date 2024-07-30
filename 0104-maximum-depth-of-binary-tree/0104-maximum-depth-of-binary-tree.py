# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(root, curr):
            nonlocal ans
            if root is None:
                return 0
            dfs(root.left, curr +  1)
            dfs(root.right, curr + 1)
            ans = max(ans, curr)
        dfs(root, 1)
        return ans
        