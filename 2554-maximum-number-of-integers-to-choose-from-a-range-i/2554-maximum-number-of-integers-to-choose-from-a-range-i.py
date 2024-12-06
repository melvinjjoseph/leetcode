class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        bannedSet=set()
        for ban in banned:
            if ban<=n:
                bannedSet.add(ban)
        i=1
        curSum=0
        res=0
        while i<=n and curSum<maxSum:
            if i not in bannedSet:
                curSum+=i
                res+=1
            i+=1
        
        return res if curSum<=maxSum else res-1