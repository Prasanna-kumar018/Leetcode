class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        g = collections.defaultdict(list)
        for x,y in edges:
            g[x].append(y)
            g[y].append(x)
        d= collections.defaultdict(int)
        def get(start):
            nonlocal n
            q = collections.deque([start])
            res = [-1]*(n+1)
            res[start]= 1
            level = 0
            root = start
            while q:
                size = len(q)
                while size>0:
                    x = q.popleft()
                    root = min(root,x) # FOR EACH GROUP UNIQUE SMALLEST ELEMENT MUST PRESENT
                    for des in g[x]:
                        if res[des]==-1:
                            res[des]=res[x]+1
                            q.append(des)
                        else:
                            if abs(res[des]-res[x])!=1:
                                return  -1
                    size-=1
                level+=1
            d[root]=max(d[root],level)
        for i in range(1,n+1):
            if get(i)==-1: # if one can't do then others in the group can not do for sure....
                return -1 # So any one group can't make it then no other group can make this
        print(d)
        return sum(d.values())