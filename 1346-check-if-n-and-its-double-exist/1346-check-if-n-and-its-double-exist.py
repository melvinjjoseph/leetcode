class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        setArr=set(arr)
        count0=arr.count(0)
        for ele in arr:
            if ele==0 and count0>1:
                return True 
            elif ele!=0 and ele*2 in setArr:
                return True
        return False