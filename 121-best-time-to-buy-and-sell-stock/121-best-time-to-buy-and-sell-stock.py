class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=0
        buym=0
        sell=1
        maxp=0
        for i in range(0,len(prices)-1):
            if (prices[sell]-prices[buym])>maxp:
                maxp=prices[sell]-prices[buym]
            buy=buy+1
            sell=sell+1
            if prices[buym]>=prices[buy]:
                    buym=buy
                    
        return maxp