class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        maxi=(r-l)*min(height[l],height[r])
        while(l<r):
            if height[l]<height[r]:
                l=l+1
            else: 
                r=r-1
            new=(r-l)*min(height[l],height[r])
            maxi=max(maxi,new)
        return maxi


