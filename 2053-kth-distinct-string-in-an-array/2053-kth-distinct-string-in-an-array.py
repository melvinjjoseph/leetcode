class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts=defaultdict(int)
        for ele in arr:
            counts[ele]+=1
        for ele in arr:
            if counts[ele]==1:
                k-=1
            if k==0:
                return ele
        return ""