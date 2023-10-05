class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1, count2=0,0
        candidate1, candidate2=0,0
        for num in nums:
            if num==candidate1:
                count1+=1
            elif num==candidate2:
                count2+=1
            elif count1==0 and num!=candidate2:
                count1=1
                candidate1=num
            elif count2==0 and num!=candidate1:
                count2=1
                candidate2=num
            else:
                count1-=1
                count2-=1
        res=[]
        threshold=len(nums)//3
        count1, count2=0,0
        for num in nums:
            if candidate1==num:
                count1+=1
            elif candidate2==num:
                count2+=1
        if count1>threshold:
            res.append(candidate1)
        if count2>threshold:
            res.append(candidate2)
        return res