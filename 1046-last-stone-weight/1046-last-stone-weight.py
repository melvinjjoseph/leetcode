class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while(len(stones)>1):
            m1=stones.pop()
            if len(stones)==0:
                return m1
            m2=stones.pop()
            if m1>m2:
                m=m1-m2
                if len(stones)==0:
                    return m
                insort_left(stones,m)
        try:
            return stones[0]
        except:
            return 0
        