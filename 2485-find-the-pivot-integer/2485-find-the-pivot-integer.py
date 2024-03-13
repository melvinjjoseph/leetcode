class Solution:
    def pivotInteger(self, n: int) -> int:
        if n==1:
            return n
        l=1
        r=n
        l_sum=l
        r_sum=r
        while l<r:
            if r_sum>l_sum:
                l_sum+=l+1
                l+=1
            else:
                r_sum+=r-1
                r-=1
            if l_sum==r_sum and l+1==r-1:
                return l+1
        return -1
            