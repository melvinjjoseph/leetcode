class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        counts=defaultdict(int)
        for ele in arr:
            counts[ele%k]+=1
        for ele, c in counts.items():
            if ele==0 or (ele==k/2 and k%2==0):
                if c%2==1:
                    return False
            elif c!=counts[abs(ele-k)]:
                return False
        return True