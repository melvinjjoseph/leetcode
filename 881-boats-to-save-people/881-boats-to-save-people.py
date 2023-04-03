class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count=0
        i=0
        j=len(people)-1
        while(j>=i):
            if people[i]+people[j]<=limit:
                count+=1
                j-=1
                i+=1
            else:
                count+=1
                j-=1
        return count
        
        
        