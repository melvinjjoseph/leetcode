class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1=min(prices)
        prices.remove(min1)
        min2=min(prices)
        prices.remove(min2)
        if min1+min2<=money:
            return money-min1-min2
        else:
            return money