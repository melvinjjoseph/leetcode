# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        sums=[]
        q=deque()
        q.append(root)
        while q:
            n=len(q)
            s=0
            for _ in range(n):
                popped=q.popleft()
                s+=popped.val
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)
            heapq.heappush(sums,-s)
        if len(sums)<k:
            return -1
        for _ in range(k-1):
            heapq.heappop(sums)
        return -heapq.heappop(sums)