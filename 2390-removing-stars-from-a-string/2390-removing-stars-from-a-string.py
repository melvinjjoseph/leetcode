class Solution:
    def removeStars(self, s: str) -> str:
        # strList=list(map(str,s))
        # i=0
        # while(i<len(strList)):
        #     if strList[i]=='*':
        #         strList.pop(i)
        #         strList.pop(i-1)
        #         i-=1
        #     else:
        #         i+=1
        strList=[]
        for ele in s:
            if ele!='*':
                strList.append(ele)
            else:
                strList.pop()
        if len(strList)==0:
            return ""
        op=''.join([str(elem) for i,elem in enumerate(strList)])
        return op
        print(strList)