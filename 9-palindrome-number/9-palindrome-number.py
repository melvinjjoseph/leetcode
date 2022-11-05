class Solution:
    def isPalindrome(self, x: int) -> bool:
        check=x
        num=0
        while x>0:
            num=num*10
            num=num+(x%10)
            
            x=x//10
        if num==check:
            return True
        else :
            return False
        