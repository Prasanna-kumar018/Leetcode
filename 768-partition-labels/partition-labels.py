class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for idx,val in enumerate(s):
            last[val]=idx
        i = 0
        n = len(s)
        res = []
        while i<n:
            start = i
            curr = last[s[i]]
            while i<=curr:
                curr = max(curr,last[s[i]])
                i+=1
            res.append(curr-start+1)
        return res