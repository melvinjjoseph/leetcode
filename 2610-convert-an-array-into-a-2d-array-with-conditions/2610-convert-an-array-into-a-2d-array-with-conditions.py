class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        counter=[0]*201
        added=0
        res=[]
        for i in nums:
            counter[i]+=1
            added+=1
        while added:
            toadd=[]
            for i in range(len(counter)):
                if counter[i]>0:
                    toadd.append(i)
                    counter[i]-=1
                    added-=1
            res.append(toadd)
        return res
        