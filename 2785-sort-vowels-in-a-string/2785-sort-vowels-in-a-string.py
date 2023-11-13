class Solution:
    def sortVowels(self, s: str) -> str:
        vowels=['a','e','i','o','u','A','E','I','O','U']
        added=[]
        new=""
        for i in range(len(s)):
            if s[i] in vowels:
                added.append(s[i])
                new+='_'
            else:
                new+=s[i]
        s=''
        added.sort()
        added=collections.deque(added)
        for i in range(len(new)):
            if new[i]=='_':
                s+=added.popleft()
            else:
                s+=new[i]
        return s