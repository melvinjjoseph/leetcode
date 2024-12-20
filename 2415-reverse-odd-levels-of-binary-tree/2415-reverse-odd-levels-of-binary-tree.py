# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def swap(self,node1, node2):
            node1.left,node1.right=node2.right,node2.left
        if not root:
            return root
        q=deque([root])
        n=0
        while q:
            l=len(q)
            if n%2==1:
                for i in range(l//2):
                    q[i].val,q[-i-1].val=q[-i-1].val,q[i].val
            for i in range(l):
                popped=q.popleft()
                if popped.left and popped.right:
                    q.append(popped.left)
                    q.append(popped.right)
            n+=1
        return root