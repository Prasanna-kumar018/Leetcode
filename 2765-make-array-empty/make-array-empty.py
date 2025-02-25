class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        n = len(nums)
        res = n
        arr = [(val,idx) for idx,val in enumerate(nums)]
        tree = [0]*(n+1)
        arr.sort()
        def get(idx):
            s = 0
            while idx>0:
                s+=tree[idx]
                idx-=(idx&(-idx))
            return s
        def update(idx):
            while idx<=n:
                tree[idx]+=1
                idx+=(idx&(-idx))
        res+=arr[0][1]
        update(arr[0][1]+1)
        # print(arr)
        for i in range(n-1):
            x,y = arr[i][1] , arr[i+1][1]
            if x < y:
                # print(get(y)-get(x+1))
                res+=(y-x-1)-(get(y)-get(x+1))
            else: # x > y
                # print((n-1-x+y),(get(n)-get(x+1))+get(y))
                res += (n-1-x+y)- (get(n)-get(x+1))-(get(y))
            update(y+1)
            # print(res,"res")
        return res