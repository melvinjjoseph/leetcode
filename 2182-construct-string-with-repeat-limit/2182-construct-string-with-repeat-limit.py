class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counts=defaultdict(int)
        for char in s:
            counts[char]+=1
        minheap=[(-ord(c), counts[c]) for c in counts]
        heapq.heapify(minheap)
        res=""
        while minheap:
            maxi,c=heapq.heappop(minheap)
            char=chr(-maxi)
            while c:
                remove=min(repeatLimit,c)
                c=c-remove
                res+=char*remove
                if c==0:
                    break
                if not minheap:
                    return res
                max2,c2=heapq.heappop(minheap)
                char2=chr(-max2)
                c2-=1
                res+=char2
                if c2:
                    heapq.heappush(minheap,(-ord(char2), c2))
        return res