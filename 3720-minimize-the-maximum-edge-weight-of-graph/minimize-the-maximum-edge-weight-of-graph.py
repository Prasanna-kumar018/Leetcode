class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        g = collections.defaultdict(list)
        MX = 0
        for x,y,w in edges:
            g[y].append((x,w))
            MX = max(MX,w)
        def isSafe(wt):
            q = collections.deque()
            q.append(0)
            done = set()
            done.add(0)
            while q:
                node = q.popleft()
                for des,w in g[node]:
                    if w<=wt and des not in done:
                        q.append(des)
                        done.add(des)
            if len(done)!=n:
                return False
            return True
        l,r = 0,MX
        ans = -1
        while l<=r:
            mid = (l+r)//2
            if isSafe(mid):
                r = mid-1
                ans = mid
            else:
                l = mid+1
        return ans