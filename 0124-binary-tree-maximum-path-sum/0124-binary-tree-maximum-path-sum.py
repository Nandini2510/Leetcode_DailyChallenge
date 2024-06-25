# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        currSum = float("-inf")

        def dfs(root):
            nonlocal currSum
            if root is None:
                return 0
            
            leftSum = dfs(root.left)
            rightSum = dfs(root.right)
            leftSum = max(leftSum, 0)
            rightSum = max(rightSum, 0)
            currSum = max(currSum, root.val + leftSum + rightSum) 

            return root.val + max(rightSum, leftSum)
        dfs(root)
        return currSum