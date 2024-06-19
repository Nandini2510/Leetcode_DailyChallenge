# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = root
        def dfs(curr, minEl, maxEl):
            nonlocal ans
            if curr is None:
                return
            if p.val >= minEl and q.val <= maxEl and q.val >= minEl and p.val <= maxEl:
                ans = curr
            dfs(curr.left, minEl, curr.val - 1)
            dfs(curr.right, curr.val + 1, maxEl)   
        
        dfs(root,float("-inf"), float("inf"))
        return ans