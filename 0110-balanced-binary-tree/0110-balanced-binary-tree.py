# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        flag = True

        def dfs(root):
            nonlocal flag
            if root is None:
                return 0
            lh = dfs(root.left)
            rh = dfs(root.right)
            if abs(rh - lh) > 1:
                flag = False
            return 1 + max(lh, rh)
        dfs(root)
        return flag
        
        