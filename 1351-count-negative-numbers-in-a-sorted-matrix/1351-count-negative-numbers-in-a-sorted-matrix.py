class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        for l in grid:
            i=1
            while i<=len(l) and l[-i]<0:
                count+=1
                i+=1
        return count 
        