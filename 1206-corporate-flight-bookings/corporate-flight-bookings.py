class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        """
        We can do range addition using sweep line very easily but we are going to 
        try this range addition in fenwick tree

        arr = [0]*(n+1)
        for x,y,z in bookings:
            arr[x]+=z
            if y+1<=n:
                arr[y+1]-=z
        for i in range(1,n+1):
            arr[i]+=arr[i-1]
        return arr[1:]

        """

        tree1 = [0]*(n+1)
        tree2 = [0]*(n+1)
        def update(tree,idx,val):
            while idx<=n:
                tree[idx]+=val
                idx += (idx&(-idx))
        def updateit(x,y,z):
            update(tree1,x,z)
            update(tree1,y+1,-z)
            update(tree2,x,-(x-1)*z)
            update(tree2,y+1,y*z)
        def get(tree,idx):
            s = 0
            while idx>0:
                s += tree[idx]
                idx -= (idx&(-idx))
            return s
        def gett(idx):
            return get(tree1,idx)*idx + get(tree2,idx)

        def getit(l,r):
            return gett(r)-gett(l-1) 
        for x,y,z in bookings:
            updateit(x,y,z)
        
        res = []
        for i in range(1,n+1):
            res.append(getit(i,i))
        return res
        