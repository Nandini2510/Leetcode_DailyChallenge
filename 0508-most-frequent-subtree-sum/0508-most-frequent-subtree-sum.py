# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        s = 0
        mp = defaultdict(int)
        maxCount = 0
        res = []
        def dfs(root):
            nonlocal s
            nonlocal maxCount
            if root is None:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            s = root.val + l + r
            mp[s] += 1
            maxCount = max(maxCount, mp[s])
            return s
        dfs(root)
        for key, val in mp.items():
            if val == maxCount:
                res.append(key)

        return res