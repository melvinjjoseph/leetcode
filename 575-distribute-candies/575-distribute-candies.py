class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n=len(candyType)
        candyTypeSet=set(candyType)
        if(len(candyTypeSet)>=n/2):
            return n//2
        else :
            return len(candyTypeSet)
        