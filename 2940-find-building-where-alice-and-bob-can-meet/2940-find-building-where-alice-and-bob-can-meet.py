class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        ans=[-1]*len(queries)
        groups=defaultdict(list)
        for i,q in enumerate(queries):
            l,r=sorted(q)
            if l==r or heights[r]>heights[l]:
                ans[i]=r
            else:
                h=max(heights[r], heights[l])
                groups[r].append((h,i))
        minheap=[]
        
        for i,h in enumerate(heights):
            for qh,qi in groups[i]:
                heapq.heappush(minheap,(qh,qi))
            while minheap and h>minheap[0][0]:
                qh,qi=heapq.heappop(minheap)
                ans[qi]=i
            
        return ans
            