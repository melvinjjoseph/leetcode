class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i,ele in enumerate(haystack):
            if needle[0]==ele:
                print(i)
                hay=haystack[i:i+len(needle)]
                if hay==needle:
                    return i
        return -1