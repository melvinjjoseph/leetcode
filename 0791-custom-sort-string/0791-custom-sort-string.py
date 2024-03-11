class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counts=defaultdict(int)
        for i in s:
            counts[i]+=1
        res=""
        for i in order:
            res=res+(i*counts[i])
            counts[i]=0
        for i in counts:
            if counts[i]>0:
                res=res+(i*counts[i])
        return res