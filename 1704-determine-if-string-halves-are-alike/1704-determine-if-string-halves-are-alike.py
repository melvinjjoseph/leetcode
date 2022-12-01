class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a=s[0:len(s)//2]
        b=s[len(s)//2:len(s)]
        #print(a,b)
        vowels=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        a_vowels=0
        b_vowels=0
        a_conso=0
        b_conso=0
        for i in range(len(s)//2):
            if a[i] in vowels:
                a_vowels=a_vowels+1
            else:
                a_conso=a_conso+1
            if b[i] in vowels:
                b_vowels=b_vowels+1
            else:
                b_conso=b_conso+1
        if a_vowels==b_vowels and a_conso==b_conso:
            return True
        else: 
            return False