class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        hmap=defaultdict(int)
        for s in chars:
            if s not in hmap:
                hmap[s]=1
            else:
                hmap[s]+=1
        ans=0
        for word in words:
            wordCount=defaultdict(int)
            for w in word:
                if w not in wordCount:
                    wordCount[w]=1
                else:
                    wordCount[w]+=1
            
            isTrue=True
            for letter in wordCount:
                if wordCount[letter]>hmap[letter]:
                    isTrue=False
            if isTrue:
                ans+=len(word)
        return ans