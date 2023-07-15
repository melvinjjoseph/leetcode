class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)-1
        cost.append(0)
        cost.append(0)
        while n>-1:
            cost[n]=cost[n]+min(cost[n+1], cost[n+2])
            n-=1
            
        print(cost)
        return min(cost[0], cost[1])
            
                