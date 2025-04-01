# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        result = []

        def postorder(node):

            # visting the left sub-tree
            postorder(node.left)

            # visting the right sub-tree
            postorder(node.right)
            
            # visiting the root node first
            result.append(node.val)            
        
        postorder(root)
        return result