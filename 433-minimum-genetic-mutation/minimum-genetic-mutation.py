class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        q = collections.deque()
        q.append(startGene)
        level = 0
        def istrue(x,y):
            l = len(x)
            c = 0
            for i in range(l):
                if x[i]!=y[i]:
                    c+=1
            return True if c==1 else False
        vis = set()
        while q:
            size = len(q)
            while size>0:
                start  = q.popleft()
                if start==endGene:
                    return level
                if start in vis:
                    size-=1
                    continue
                vis.add(start)
                for x in bank:
                    if x not in vis and istrue(start,x):
                        q.append(x)
                size-=1
            level+=1
        return -1