# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        queue = [root]
        level = 0
        while queue:
            level += 1
            temp = []
            for i in queue:
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            if level % 2 != 0:
                l = len(temp)
                for i in range(l // 2):
                    temp[i].val, temp[l-i-1].val = temp[l-i-1].val, temp[i].val
            queue = temp
        return root
