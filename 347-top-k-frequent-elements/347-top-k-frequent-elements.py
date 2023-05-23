class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap={}
        for i in nums:
            if i not in hmap:
                hmap[i]=1
            else:
                hmap[i]+=1
        freq=[[] for i in range(len(nums)+1)]
        for n,c in hmap.items():
            freq[c].append(n)
        op=[]
        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                op.append(j)
                if len(op)==k:
                    return op
        
        
        
        