class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy=max(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies>=maxCandy:
                candies[i]=True
            else:
                candies[i]=False
        return candies
        