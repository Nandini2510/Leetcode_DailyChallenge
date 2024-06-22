# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = True

        def dfs(root, minVal, maxVal):
            if root is None:
                return
            nonlocal ans
            if root.val < minVal or root.val > maxVal:
                ans = False
                return
            dfs(root.left, minVal, root.val - 1)
            dfs(root.right, root.val + 1, maxVal)
            
        dfs(root, float("-inf"), float("inf"))
        return ans