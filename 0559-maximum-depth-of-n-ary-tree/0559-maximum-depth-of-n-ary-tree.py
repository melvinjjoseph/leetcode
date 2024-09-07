"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(root, count):
            if root is None:
                return 0
            maxi=0
            for c in root.children:
                maxi=max(maxi, dfs(c,count))
                # print(maxi)
            return maxi+1
        return dfs(root,0)
        