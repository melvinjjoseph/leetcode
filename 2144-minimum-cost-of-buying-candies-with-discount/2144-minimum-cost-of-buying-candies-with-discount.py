class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        res=0
        for i in range(len(cost)-1,-1,-3):
            res=res+cost[i]
            if i-1>=0:
                res+=cost[i-1]
        return res
            