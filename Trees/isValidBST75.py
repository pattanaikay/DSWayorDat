# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, min_val=float('-inf'), max_val=float('inf')):
            if not node:
                return True
            
            if node.val <= min_val or node.val >= max_val:
                return False
            
            # validate left tree, must be less than current node and validate right tree, must be greater than current node
            return validate(node.left, min_val, node.val) and \
                validate(node.right, node.val, max_val)

        return validate(root)