class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        d = collections.Counter(word1)
        e = collections.Counter(word2)
        x = collections.Counter(d.values())
        y = collections.Counter(e.values())
        return x==y and set(d.keys())==set(e.keys())