class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        d = collections.defaultdict(int)
        for x,y in zip(chars,vals):
            d[x]=y
        for i in range(26):
            c = chr(ord('a')+i)
            if c not in d:
                d[c]=i+1
        curr = maxi = 0
        for x in s:
            curr += d[x]
            maxi = max(maxi,curr)
            if curr<0:
                curr = 0
        return maxi