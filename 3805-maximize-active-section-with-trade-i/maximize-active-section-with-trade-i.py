class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ans = s.count('1')
        s = '1'+ s + "1"
        n = len(s)
        prefix = [0]
        for i in range(1,n-1):
            prefix.append(prefix[-1]+(1 if s[i]=='1' else 0))
        prefix.append(prefix[-1])
        suffix = [0]

        for i in range(n-2,0,-1):
            suffix.append(suffix[-1]+(1 if s[i]=='1' else 0))
        suffix.append(suffix[-1])
        suffix.reverse()
        start = []
        end = []
        i = 0
        while i<n:
            if s[i]=='1':
                start.append(i)
                while i+1<n and s[i+1]=='1':
                    i+=1
                end.append(i)
            i+=1
        m = len(start)
        for i in range(m-2):
            val = 1 if i==0 else 0
            val += 1 if i+2 == m-1 else 0
            left = prefix[start[i]-1] if start[i]-1>=0 else 0
            right = (suffix[end[i+2]+1] if end[i+2]+1<n else 0 )
            ans = max(ans,end[i+2]-start[i]+1-val+left+right)
        return ans