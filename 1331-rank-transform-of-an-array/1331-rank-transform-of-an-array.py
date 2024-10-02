class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr1=list(set(arr))
        ranks={}
        arr1.sort()
        for i in range(len(arr1)):
            ranks[arr1[i]]=i+1
        res=[]
        for ele in arr:
            res.append(ranks[ele])
        return res