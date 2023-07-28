class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hashmap={}
        if len(hand)%groupSize!=0:
            return False
        for ele in hand:
            if ele not in hashmap:
                hashmap[ele]=1
            else:
                hashmap[ele]+=1
        minHeap=list(hashmap.keys())
        heapq.heapify(minHeap)
        while minHeap:
            popped= minHeap[0]
            hashmap[popped]-=1
            if hashmap[popped]==0:
                heapq.heappop(minHeap)
            for i in range(1,groupSize):
                if popped+i not in hashmap:
                    return False
                if hashmap[popped+i]==0:
                    return False
                hashmap[popped+i]-=1
                if hashmap[popped+i]==0:
                    heapq.heappop(minHeap)
        return True