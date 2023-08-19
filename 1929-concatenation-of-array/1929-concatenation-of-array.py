class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # nums1=nums.copy()
        nums.extend(nums)
        return nums