class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels=['a','A','e','E','i','I','o','O','u','U']
        a=s[:len(s)//2]
        b=s[len(s)//2:]
        c1=0
        c2=0
        for i in a:
            if i in vowels:
                c1+=1
        for i in b:
            if i in vowels:
                c2+=1
        return c1==c2