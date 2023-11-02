# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        Count=0
        def dfs(root):
            nonlocal Count
            if root is None:
                return [0,0]
            lsum,lc=dfs(root.left)
            rsum,rc=dfs(root.right)
            
            val=lsum+rsum+root.val
            c=lc+rc+1
            
            if val//c==root.val:
                Count+=1
            return [val,c]
            
        dfs(root)
        return Count