# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = float("-inf")

        def dfs(root):
            nonlocal res
            if not root:
                return 0
            leftSum = dfs(root.left)
            rightSum = dfs(root.right)
            leftSum = max(leftSum, 0)
            rightSum = max(rightSum, 0)
            res = max(res, root.val + leftSum + rightSum)

            return root.val + max(leftSum, rightSum)
        dfs(root)
        return res
        