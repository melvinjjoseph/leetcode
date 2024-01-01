class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        satisfied=0
        j=0
        for c in s:
            if j<len(g) and c>=g[j]:
                satisfied+=1
                j+=1
        return satisfied