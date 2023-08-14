class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        if not len(nums):
            return ans
        num = nums[0]
        temp = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == temp+1:
                temp = nums[i]
            else:
                if (temp - num) >= 1:
                       ans.append(f"{num}->{temp}")
                else:
                    ans.append(str(num))
                num = nums[i]
                temp = nums[i]
        if (temp - num) >= 1:   
            ans.append(f"{num}->{temp}")
        else:
            ans.append(str(num))
        return ans
        