class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        n = len(words)
        INF = 10**20
        dp = [[INF]*n for _ in range(n)]
        for i in range(n):
            for j in range(i,n):
                l = 0
                for k in range(i,j+1):
                    l+=len(words[k])
                l+=(j-i) # spaces
                if l<=maxWidth:
                    dp[i][j]=maxWidth-l
        go = {}
        res = [ INF for _ in range(n)]
        for i in range(n):
            idx = -1
            for j in range(i+1):
                val = dp[j][i]+(res[j-1] if j-1>=0 else 0)
                if val<=res[i]:
                    res[i]=val
                    idx = j
            go[i]=idx
        # print(go)
        index = n-1
        res = []
        while index in go:
            s = []
            start = go[index]
            rem = maxWidth
            for i in range(start,index+1):
                rem-=len(words[i])
            rem-=(index-start)
            whole = rem//(index-start) if index-start!=0 else 0
            t = rem%(index-start) if index-start!=0 else 0            
            # print(rem,whole,t)
            if index==n-1:
                for i in range(start,index+1):
                    s.append(words[i])
                    s.append(" ")
                s.pop()
                s.append(' '*(rem)) # if rem==0
            else:
                for i in range(start,index+1):
                    if i!=index:
                        s.append(words[i]+" ")
                        a = whole+(1 if (i-start)<t else 0)
                        s.append(" "*a)
                        rem-=(a)
                    else:
                        s.append(words[i]+(" "*rem))
            res.append(''.join(s))
            index = start-1
        res.reverse()
        return res