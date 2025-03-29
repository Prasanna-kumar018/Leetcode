class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        n = len(s)
        first = {}
        last = {}
        for idx,c in enumerate(s):
            if c not in first:
                first[c]=idx
            last[c]=idx

        for c in first.keys():
            left = first[c]
            right = last[c]
            q= collections.deque()
            for i in range(left,right):
                q.append(i)
            
            while q:
                x = q.popleft()
                lx = first[s[x]]
                rx = last[s[x]]
                for i in range(lx,left):
                    q.append(i)
                for i in range(right,rx):
                    q.append(i)
                left = min(left,lx)
                right = max(right,rx)
            first[c]=left
            last[c]=right
        
        q = []
        def push(val):
            heapq.heappush(q,val)
        def pop():
            return heapq.heappop(q)
        for c in first.keys():
            if not (first[c]==0 and last[c]==n-1):
                push((first[c],c,1,0))
        # d =1 for first and -1 for last
        most = 0
        while q:
            _ , c, d,val = pop()
            if d==1:
                push((last[c],c,-1,most+1))
            else:
                most = max(most,val)
        return most>=k
