class Solution:
    def reorganizeString(self, s: str) -> str:
        hashmap={}
        for ele in s:
            if ele not in hashmap:
                hashmap[ele]=1
            else:
                hashmap[ele]+=1
        minHeap=[]
        for ele in hashmap.keys():
            minHeap.append([(-1*hashmap[ele]),ele])
        heapq.heapify(minHeap)
        op=''
        prevEle=[]
        while minHeap:
            eleVal,eleStr=heapq.heappop(minHeap)
            if prevEle:
                heapq.heappush(minHeap,prevEle)
            op+=eleStr
            eleVal+=1
            if eleVal<0:
                prevEle=[eleVal,eleStr]
            else:
                prevEle=[]
        if len(s)==len(op):
            return op
        return ''