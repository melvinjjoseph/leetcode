class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        op=collections.deque()
        for i in nums:
            if i%2:
                op.append(i)
            else:
                op.appendleft(i)
        return op