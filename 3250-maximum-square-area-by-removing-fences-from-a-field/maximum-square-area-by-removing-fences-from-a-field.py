class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        h= set(hFences)
        mod = pow(10,9)+7
        v = set(vFences)
        h.add(1)
        h.add(m)
        v.add(1)
        v.add(n)
        hori = set()
        vert = set()
        for i in h:
            for j in h:
                hori.add(abs(j-i))

        for i in v:
            for j in v:
                vert.add(abs(j-i))

        ans = float('-inf')
        for i in vert:
            if i in hori:
                ans= max(ans, i*i)
        return -1 if ans ==0 else ans%mod # because if i and j are same 0 would exist for sure
