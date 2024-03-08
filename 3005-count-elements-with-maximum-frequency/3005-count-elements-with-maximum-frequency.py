class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        element_count=defaultdict(int)
        for num in nums:
            element_count[num]+=1
        max_ele=0
        max_count=0
        for c in element_count:
            if element_count[c]>max_ele:
                max_ele=element_count[c]
                max_count=1
            elif element_count[c]==max_ele:
                max_ele=element_count[c]
                max_count+=1
        return max_ele*max_count