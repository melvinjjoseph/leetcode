class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        li=[]
        for ele in pushed:
            li.append(ele)
            while len(popped)>0 and len(li)>0 and li[-1]==popped[0]:
                popped.pop(0)
                li.pop()
        if len(popped)==len(li) and len(li)==0:
            return True
        return False