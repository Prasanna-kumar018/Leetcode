class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if Counter(s1)!=Counter(s2):
            return False
        count = 0
        for x,y in zip(s1,s2):
            if x!=y:
                count+=1
        return True if count<=2 else False