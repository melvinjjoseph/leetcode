class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # pos=[0]*len(arr)
        chunk=0
        set1=set()
        set2=set()
        for i in range(len(arr)):
            set1.add(i)
            set2.add(arr[i])
            if set1==set2:
                chunk+=1
        return chunk