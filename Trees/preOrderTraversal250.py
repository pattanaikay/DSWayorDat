# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        result = []

        def preorder(node):
            
            # visiting the root node first
            result.append(node.val)

            # visting the left sub-tree
            preorder(node.left)

            # visting the right sub-tree
            preorder(node.right)
        
        preorder(root)
        return result