# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0

        def dfs(root, maxNode):
            if root is None:
                return 0
            nonlocal ans
            if root.val >= maxNode:
                ans += 1
                maxNode = root.val
            dfs(root.left, maxNode)
            dfs(root.right, maxNode)
        dfs(root, float("-inf"))
        return ans

        