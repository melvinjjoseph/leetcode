class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        op=[]
        m=len(potions)
        maxPotion=potions[-1]
        for i in spells:
            minPotion=ceil(success/i)
            if minPotion>maxPotion:
                op.append(0)
                continue
            index=bisect.bisect_left(potions,minPotion)
            op.append(m-index)
        return op
                