class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        hashmap=defaultdict(int)
        for ele in nums:
            hashmap[ele]+=1
            if hashmap[ele]==2:
                res.append(ele)
        return res
        