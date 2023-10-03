class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashmap=defaultdict(int)
        for ele in nums:
            hashmap[ele]+=1
        count=0
        for c in hashmap.values():
            count+=(c*(c-1)//2)
        return count