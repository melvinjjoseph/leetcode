class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count=0
        for i in range(len(strs[0])):
            for s in range(len(strs)-1):
                if strs[s][i]>strs[s+1][i]:
                    count+=1
                    break
        return count
