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
        deq=collections.deque()
        deq.append(root)
        while deq:
            leng=len(deq)
            t=float("-inf")
            for i in range(leng):
                popped=deq.popleft()
                if popped.val>t:
                    t=popped.val
                if popped.left:
                    deq.append(popped.left)
                if popped.right:
                    deq.append(popped.right)
            ans.append(t)
        return ans
                