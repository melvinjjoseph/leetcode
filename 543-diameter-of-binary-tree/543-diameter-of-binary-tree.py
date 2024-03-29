# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        
        def dfs(root):
            if root is None:
                return -1
            left=dfs(root.left)
            right=dfs(root.right)
            res[0]=max(res[0],2+left+right)
            return 1+max(left,right)
        res=[0]
        dfs(root)
        return res[0]
            
            
        