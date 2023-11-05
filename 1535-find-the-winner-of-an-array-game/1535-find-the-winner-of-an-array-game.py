class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        dq=collections.deque(arr)
        maxEle=max(arr)
        winner=dq.popleft()
        winCount=0
        while dq:
            comp=dq.popleft()
            if winner>comp:
                winCount+=1
                dq.append(comp)
            else:
                winCount=1
                dq.append(winner)
                winner=comp
            if winCount==k or winner==maxEle:
                return winner