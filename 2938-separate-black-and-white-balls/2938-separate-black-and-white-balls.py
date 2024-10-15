class Solution:
    def minimumSteps(self, s: str) -> int:
        black=0
        swaps=0
        for ch in s:
            if ch=="0":
                swaps+=black
            else:
                black+=1
        return swaps