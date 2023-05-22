class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap={}
        for i in nums:
            if i not in hmap:
                hmap[i]=1
            else:
                hmap[i]+=1
        op=[]
        for i in range(k):
            maxi=0
            for j in hmap:
                if hmap[j]>maxi:
                    maxi=hmap[j]
                    maxval=j
            hmap[maxval]=0
            op.append(maxval)
        return op
        
        
        
        