class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n =  len(words)
        INF = 10**20
        demo = {}
        @cache
        def recur(prev,idx):
            if idx==n:
                return 0
            res = recur(prev,idx+1)
            demo[(prev,idx)]=(prev,idx+1,-1)
            if groups[prev]!=groups[idx]:
                v = recur(idx,idx+1)+1
                if v>res:
                    res = v
                    demo[(prev,idx)]=(idx,idx+1,idx)
            return res
        ans = 0
        start = -1
        for i in range(n):
            vv = recur(i,i+1)+1
            if vv > ans:
                ans = vv
                start = i
        sec = start+1
        res = [words[start]]
        while (start,sec) in demo:
            (ns,nsec,ind)= demo[(start,sec)]
            if ind!=-1:
                res.append(words[ind])
            start, sec = ns,nsec
        return res