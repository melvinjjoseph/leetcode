class Solution:
    def removeStars(self, s: str) -> str:
        strList=[]
        for ele in s:
            if ele!='*':
                strList.append(ele)
            else:
                strList.pop()
        op=''.join([str(elem) for i,elem in enumerate(strList)])
        return op