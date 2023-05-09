class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        dict={}
        for i in nums:
            if i not in dict:
                dict[i]=1
            else:
                dict[i]+=1
        for i in dict:
            if dict[i]>len(nums)/2:
                return i