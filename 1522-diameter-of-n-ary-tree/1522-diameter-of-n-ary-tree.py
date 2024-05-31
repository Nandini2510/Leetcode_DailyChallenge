"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        if root is None:
            return 0
        ans = 0
        s = 0
        def dfs(node):
            nonlocal ans
            if not len(node.children):
                return 1
            p = []
            for child in node.children:
                p.append(dfs(child))
            ans = max(ans, sum(heapq.nlargest(2,p)))
            return max(p) + 1
        dfs(root)
        return ans
