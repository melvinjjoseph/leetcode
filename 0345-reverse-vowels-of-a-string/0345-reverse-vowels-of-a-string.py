class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=['a','e','i','o','u','A','E','I','O','U']
        add=[]
        for ele in s:
            if ele in vowels:
                add.append(ele)
        add=add[::-1]
        new=''
        i=0
        for ele in s:
            if ele in vowels:
                new+=add[i]
                i+=1
            else:
                new+=ele
        return new