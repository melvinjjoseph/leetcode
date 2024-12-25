# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans=[]
        q=deque([root])
        while q:
            n=len(q)
            row=[]
            for i in range(n):
                popped=q.popleft()
                row.append(popped.val)
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)
            
            ans.append(max(row))
        return ans    