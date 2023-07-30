class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        b,h=0,0
        if length>=10000 or width>=10000 or height>=10000 or length*width*height>=10**9:
            b=1
        if mass>=100:
            h=1
        if b and h:
            return "Both"
        elif not b and not h:
            return "Neither"
        elif not b and h:
            return "Heavy"
        else:
            return "Bulky"