"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None: return 0
        ans = 0
        def dfs(node, depth):
            nonlocal ans
            if node == None:
                return
            for child in node.children:
                dfs(child, depth + 1)
            ans = max(depth, ans)
        dfs(root, 1)
        return ans