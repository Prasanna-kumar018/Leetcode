class Solution:
    def matchReplacement(self, main: str, sub: str, mappings: List[List[str]]) -> bool:
        s = collections.defaultdict(set)
        for x,y in mappings:
            s[x].add(y)
        m = len(main)
        n = len(sub)
        for i in range(m):
            j =0
            while j<n and i+j<m:
                if main[i+j]!=sub[j] and (main[i+j] not in s[sub[j]]):
                    break
                j+=1
            if j==n:
                return True
        return False 