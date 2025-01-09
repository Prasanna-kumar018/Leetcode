class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        obs  = set()
        obs.add(0)
        maxi = 0
        for x in queries:
            if x[0]==1:
                obs.add(x[1])
            maxi = max(maxi,x[1]+1)
        obs.add(maxi)
        tree = [0]*(maxi+1)
        obs = sorted(list(obs))
        prev = 0
        def update(idx,val):
            while idx<=maxi:
                tree[idx] = max(tree[idx],val) 
                idx += (idx&(-idx))
        for x in obs[1:]:
            update(x,x-prev)
            prev=x
        # print(tree)
        def get(idx):
            a = 0
            while idx>0:
                a = max(a,tree[idx])
                idx -= (idx&(-idx))
            return a
        ans = []
        s = SortedList(list(obs))
        # print(tree)
        for x in queries[::-1]:
            if x[0]==2:
                left = s.bisect_left(x[1])-1
                left = s[left]
                print(get(left),x[1]-left,left)
                val = max(get(left),x[1]-left)
                ans.append(True if val>=x[2] else False)
            else:
                left = s.bisect_left(x[1])-1
                left = s[left]
                right = s.bisect_right(x[1])
                right = s[right]
                update(right,right-left)
                s.remove(x[1])
            # print(s)
        ans.reverse()
        return ans
