class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count={}
        for i in words:
            for j in i:
                if j not in count:
                    count[j]=1
                else:
                    count[j]+=1
        n=len(words)
        for c in count:
            if count[c]%n!=0:
                return False
        return True