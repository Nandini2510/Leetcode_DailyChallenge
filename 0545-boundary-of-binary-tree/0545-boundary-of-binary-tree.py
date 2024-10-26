# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []

        def printLeft(node):
            
            if not node.left and not node.right:
                return
            
            res.append(node.val)

            if node.left:
                printLeft(node.left)
            else:
                printLeft(node.right)
            
            return
        
        def printLeaves(node):

            if not node:
                return
            
            if root != node and not node.left and not node.right:
                res.append(node.val)
                return
            
            printLeaves(node.left)
            printLeaves(node.right)

            return
        
        def printRight(node):
            
            if not node.left and not node.right:
                return
            
            if node.right:
                printRight(node.right)
            else:
                printRight(node.left)
            
            res.append(node.val)

            return
        
        res = [root.val]

        if root.left:
            printLeft(root.left)
        
        printLeaves(root)

        if root.right:
            printRight(root.right)
        
        return res