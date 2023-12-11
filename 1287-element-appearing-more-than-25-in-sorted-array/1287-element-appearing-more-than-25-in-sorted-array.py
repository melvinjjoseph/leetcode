class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        cur=-1
        countCur=0
        if len(arr)==0:
            return -1
        if len(arr)==1:
            return arr[0]
        for i in range(0,len(arr)):
            if arr[i]!=cur:
                cur=arr[i]
                countCur=1
            else:
                countCur+=1
                if countCur>len(arr)//4:
                    return cur
        return -1