class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr=""
        for i in s:
            if i.isalnum():
                newstr=newstr+i
        newstr=newstr.lower()
        return newstr==newstr[::-1]
        