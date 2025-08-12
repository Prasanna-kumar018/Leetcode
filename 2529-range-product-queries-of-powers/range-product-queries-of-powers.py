class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        power = []
        MOD = 10**9 + 7
        # while n>0:
        #     ll = int(math.log2(n))
        #     val = 2**ll
        #     power.append(val)
        #     n-=val
        # power.reverse()
        for i in range(32):
            if ((1<<i)&n) > 0:
                power.append(1<<i)
        ans = []
        for l,r in queries:
            prod = 1
            while l<=r:
                prod *= power[l]
                prod %= MOD
                l+=1
            ans.append(prod)
        return ans


