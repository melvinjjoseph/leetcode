# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q=collections.deque()
        levelOrder=[]
        q.append(root)
        while q:
            level=[]
            l=len(q)
            for i in range(l):
                popped=q.popleft()
                if popped:
                    q.append(popped.left)
                    q.append(popped.right)
                    level.append(popped.val)
            if level:
                levelOrder.append(level)
        res=[]
        for i in levelOrder:
            res.append(i[-1])
        return res
        