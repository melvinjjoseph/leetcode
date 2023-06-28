# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def isNodeSymmetric(nodeLeft,nodeRight):
            if not nodeLeft and not nodeRight:
                return True
            if not nodeLeft or not nodeRight:
                return False
            if nodeLeft.val!=nodeRight.val:
                return False
            return (isNodeSymmetric(nodeLeft.left, nodeRight.right) and isNodeSymmetric(nodeLeft.right,nodeRight.left))
        
        if root is None:
            return True
        return isNodeSymmetric(root.left,root.right)