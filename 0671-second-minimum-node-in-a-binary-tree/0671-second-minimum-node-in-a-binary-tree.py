# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        ans = set()
        if root is None:
            return -1
        def dfs(root):
            if root is None:
                return
            nonlocal ans
            dfs(root.left)
            ans.add(root.val)
            dfs(root.right)

        dfs(root)
        ans = list(ans)
        ans.sort()
        if len(ans) == 1:
            return -1
        else:
            return ans[1]
        