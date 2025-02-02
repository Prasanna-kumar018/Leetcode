class Solution:
    def maxDifference(self, s: str) -> int:
        s = collections.Counter(s)
        res = -10**20
        for x,y in s.items():
            for x1,y1 in s.items():
                if y%2!=y1%2:
                    if y1%2==1:
                        res = max(res,(y1-y))
                    else:
                        res = max(res,(y-y1))

        return res
        