class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        c=0
        for i in range(len(flowerbed)):
            if flowerbed[i]==0:
                isleftempty=(i==0) or (flowerbed[i-1]==0)
                isrigthempty= (i==len(flowerbed)-1) or (flowerbed[i+1]==0)
                if isleftempty and isrigthempty:
                    flowerbed[i]=1
                    c+=1
        return c>=n
                        
                
            
