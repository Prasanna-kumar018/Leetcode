class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # odd- even = odd , even - odd = odd
        s = 0
        ans = 0
        mod = 10**9 + 7
        d = collections.defaultdict(int)
        d[0]=1
        for x in arr:
            s+=x
            s%=2
            ans += d[(1-s)]
            d[s]+=1
        return ans%mod
            