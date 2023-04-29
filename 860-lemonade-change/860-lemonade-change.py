class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five=0
        ten=0
        for bill in bills:
            if bill==5:
                five+=1
            elif bill==10 and five>0:
                five-=1
                ten+=1
            elif bill==10 and five==0:
                return False
            else:
                if ten>0 and five>0:
                    ten-=1
                    five-=1
                elif five>2:
                    five-=3
                else:
                    return False
        return True
                
        