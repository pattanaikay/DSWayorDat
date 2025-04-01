# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        result = []

        def inorder(node):
            # first traversing through the left sub-tree
            inorder(node.left)

            # visiting the current node
            inorder(node.val)

            # traversing through the right sub-tree
            inorder(node.right)
        
        inorder(root)
        return result