# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def getCount(level):
            sortedLvl=sorted(level)
            if level==sortedLvl:
                return 0
            pos={}
            for i in range(len(sortedLvl)):
                pos[level[i]]=i
            swaps=0
            for i in range(len(level)):
                if level[i]!=sortedLvl[i]:
                    swaps+=1
                    cur=pos[sortedLvl[i]]
                    pos[level[i]]=cur
                    level[cur]=level[i]
            return swaps
        res=0
        q=deque([root])
        while q:
            n=len(q)
            level=[]
            for _ in range(n):
                popped=q.popleft()
                level.append(popped.val)
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)
            res+=getCount(level)
        return res