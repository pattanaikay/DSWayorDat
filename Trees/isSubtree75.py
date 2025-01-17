# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot) -> bool :
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        if not subRoot:
            return True
        
        if not root:
            return False
        
        # check if the current Tree matches the subroot
        if self.isSubtree(root, subRoot):
            return True
        
        # recursively check the left and right subtrees

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) 
        

    def isSameTree(self, p, q) -> bool:
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        return (p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))