class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        delY,delX=(coordinates[1][1]-coordinates[0][1]),(coordinates[1][0]-coordinates[0][0])
        for i in range(1,len(coordinates)-1):
            m1,m2=(coordinates[i+1][1]-coordinates[i][1])*delX,(coordinates[i+1][0]-coordinates[i][0])*delY
            if m1!=m2:
                return False
        return True