class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        teams=[]
        summ=skill[0]+skill[-1]
        for i in range(len(skill)//2):
            if skill[i]+skill[-(i+1)]!=summ:
                return -1
            teams.append((skill[i],skill[-(i+1)]))
        prod=0
        for a,b in teams:
            prod+=(a*b)
        return prod