# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder = []
        nodes = []

        while root is not None or nodes:
            while root is not None:
                nodes.append(root)
                root = root.left
            root = nodes.pop()
            inorder.append(root.val)
            root = root.right
        return inorder