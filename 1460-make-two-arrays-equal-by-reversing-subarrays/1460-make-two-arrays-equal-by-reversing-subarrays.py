class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        counts1=defaultdict(int)
        counts2=defaultdict(int)
        for i in arr:
            counts1[i]+=1
        for i in target:
            counts2[i]+=1
        return counts1==counts2