class Solution:

    def __init__(self, nums: List[int]):
        self.nums=nums

    def pick(self, target: int) -> int:
        output_index=[]
        for i in range(len(self.nums)):
            if self.nums[i]==target:
                output_index.append(i)
        return random.choice(output_index)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)