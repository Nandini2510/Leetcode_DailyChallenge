# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = root

        def dfs(root, minVal, maxVal):
            nonlocal ans
            if root is None:
                return 
            if minVal <= p.val and p.val <= maxVal and minVal <= q.val and q.val <= maxVal:
                ans = root
            dfs(root.left, minVal, root.val - 1)
            dfs(root.right, root.val + 1, maxVal)
        dfs(root, float("-inf"), float("inf"))
        return ans