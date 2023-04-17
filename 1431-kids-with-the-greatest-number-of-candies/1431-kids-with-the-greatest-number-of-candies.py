class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy=max(candies)
        op=[]
        for i in candies:
            if i+extraCandies>=maxCandy:
                op.append(True)
            else:
                op.append(False)
        return op
        