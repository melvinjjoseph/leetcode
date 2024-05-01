class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        try:
            end=word.index(ch)
        except:
            return word
        return word[end::-1]+word[end+1:]