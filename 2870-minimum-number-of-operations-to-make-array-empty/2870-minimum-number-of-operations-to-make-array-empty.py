class Solution:
    def minOperations(self, nums: List[int]) -> int:
        hashmap=defaultdict(int)
        for num in nums:
            hashmap[num]+=1
        res=0
        for each in hashmap:
            count=hashmap[each]
            if count==1:
                return -1
            while count:
                if count==2:
                    res+=1
                    count-=2
                elif count==3:
                    res+=1
                    count-=3
                elif count==4:
                    res+=2
                    count-=4
                else:
                    res+=1
                    count-=3
        return res
                