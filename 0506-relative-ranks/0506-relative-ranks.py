class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        hashset={}
        ranks=score.copy()
        ranks.sort()
        for i in range(1, len(ranks)+1):
            hashset[ranks[-i]]=i
        for i in range(len(score)):
            score[i]=hashset[score[i]]
            if score[i]==1:
                score[i]="Gold Medal"
            elif score[i]==2:
                score[i]="Silver Medal"
            elif score[i]==3:
                score[i]="Bronze Medal"
            else:
                score[i]=str(score[i])
        return score