import bisect
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key= lambda x:(x[0],-x[1]))
        l = []
        for x,y in envelopes:
            idx = bisect.bisect_left(l,y)
            if idx==len(l):
                l.append(y)
            else:
                l[idx]=y
        return len(l)