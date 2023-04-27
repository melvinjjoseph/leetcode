class Solution:
    def bulbSwitch(self, n: int) -> int:
        count=0
        i=1
        while(i**2<=n):
            count+=1
            i+=1
        return count
        