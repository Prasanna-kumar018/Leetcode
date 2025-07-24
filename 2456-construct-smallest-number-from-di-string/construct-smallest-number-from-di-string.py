class Solution:
    def smallestNumber(self, pattern: str) -> str:
        vis = set()
        N = len(pattern)+1
        s = []
        @cache
        def recur(idx,prev):
            if idx==N-1:
                return True
            vis.add(prev)
            for x in range(1,N+1):
                if x not in vis:
                    if pattern[idx] == 'I' and x > prev:
                        if recur(idx+1,x):
                            s.append(x)
                            return True
                    if pattern[idx] == 'D' and x< prev:
                        if recur(idx+1,x):
                            s.append(x)
                            return True
            vis.discard(prev)
            return False
        for i in range(1,N+1):
            if recur(0,i):
                s.append(i)
                break 
        s.reverse()
        return ''.join(map(str,s))