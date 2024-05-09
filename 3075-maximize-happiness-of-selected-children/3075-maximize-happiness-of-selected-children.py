class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        op=happiness[-k:]
        res=0
        turns=0
        for i in range(len(op)-1,-1,-1):
            res+=max(0,op[i]-turns)
            turns+=1
        return res