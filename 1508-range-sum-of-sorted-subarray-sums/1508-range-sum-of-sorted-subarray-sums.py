class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        Sorted=[]
        for i in range(len(nums)):
            # SortedList.add(nums[i])
            summ=0
            for j in range(i,len(nums)):
                summ+=nums[j]
                Sorted.append(summ)
        Sorted.sort()
        return sum(Sorted[left-1:right])%(10**9+7)
            