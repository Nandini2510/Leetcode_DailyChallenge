"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0
        depth = 0
        queue = [root]

        while queue:
            sz = len(queue)
            depth += 1
            for i in range(sz):
                curr = queue.pop(0)
                for node in curr.children:
                    queue.append(node)
            
        return depth