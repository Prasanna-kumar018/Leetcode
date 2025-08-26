class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l,r = 0,0
        d = collections.defaultdict(int)
        ans = 0
        while r<n:
            d[s[r]]+=1
            while d[s[r]]>1:
                d[s[l]]-=1
                l+=1
            ans = max(ans,r-l+1)
            r+=1
        return ans