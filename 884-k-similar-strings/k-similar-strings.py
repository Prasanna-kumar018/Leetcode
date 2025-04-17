class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        q =collections.deque([s1])
        n = len(s1)
        level = 0
        seen = set()
        while q:
            size= len(q)
            while size>0:
                x = q.popleft()
                if x==s2:
                    return level
                if x in seen:
                    size-=1
                    continue
                seen.add(x)
                i = 0
                x = list(x)
                while i<n and x[i]==s2[i]:
                    i+=1
                for j in range(i+1,n):
                    if x[j]==s2[i]:
                        x[i],x[j]=x[j],x[i]
                        temp= ''.join(x)
                        if temp not in seen:
                            q.append(temp)                        
                        x[i],x[j]=x[j],x[i]
                size-=1
            level+=1
        return level