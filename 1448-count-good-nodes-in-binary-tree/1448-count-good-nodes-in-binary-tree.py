# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def findCount(root,greatest):
            if root is None:
                return 0
            count=0
            if root.val>=greatest:
                count=1
            return count+findCount(root.left,max(greatest,root.val))+findCount(root.right,max(greatest,root.val))
        return findCount(root,root.val)
        