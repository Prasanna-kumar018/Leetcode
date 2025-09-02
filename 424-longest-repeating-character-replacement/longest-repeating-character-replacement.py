class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        n = len(s)
        l = res = 0
        d = collections.defaultdict(int)
        for r in range(n):
            d[s[r]]+=1
            while l<=r and (r-l+1)>(max(d.values())+k):
                d[s[l]]-=1
                l+=1
            res = max(res,r-l+1)
        return  res
