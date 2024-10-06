class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        dq1=deque(sentence1.split(" "))
        dq2=deque(sentence2.split(" "))
        while dq1 and dq2 and dq1[0]==dq2[0]:
            dq1.popleft()
            dq2.popleft()
        while dq1 and dq2 and dq1[-1]==dq2[-1]:
            dq1.pop()
            dq2.pop()
        if len(dq1)==0 or len(dq2)==0:
            return True
        return False