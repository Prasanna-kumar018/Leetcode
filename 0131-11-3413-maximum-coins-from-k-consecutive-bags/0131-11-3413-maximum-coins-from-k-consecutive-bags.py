class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        n = len(coins)
        coins.sort()
        prefix = [0]*n
        prefix[0]=coins[0][2]*(coins[0][1]-coins[0][0]+1)
        for i,(x,y,z) in enumerate(coins[1:],1):
            prefix[i]=(prefix[i-1]+(z*(y-x+1)))
        def get(x,y):
            return prefix[y]-(prefix[x-1] if x-1>=0 else 0)
        
        def find(val):
            l,r = 0, n-1
            ans = n
            while l<=r:
                mid = (l+r)//2
                if coins[mid][0]>val:
                    ans=mid
                    r =mid-1
                else:
                    l =mid+1
            return ans
        def find2(val):
            l,r = 0, n-1
            ans = -1
            while l<=r:
                mid = (l+r)//2
                if coins[mid][1]<val:
                    ans=mid
                    l =mid+1
                else:
                    r =mid-1
            return ans
        ans = 0
        # print(coins)
        for idx,(x,y,z) in enumerate(coins):
            need = find(x+k-1)

            # forward
            # print(need,"need")
            if coins[need-1][1]<=x+k-1:
                val = get(idx,need-1)
                # print(val)
                # print('f')
                ans = max(ans,val)
            else:
                val = 0
                if need-2>=idx:
                    val+= get(idx,need-2)
                s,e,g = coins[need-1]
                val+= (g*( min(e+1, x+k)-s))
                # print(val)
                ans = max(ans,val)

            need = find2(y-k+1)

            # backward
            # print(need,"need")
            if coins[need+1][0]>=y-k+1:
                val = get(need+1,idx)
                # print(val)
                # print('f')
                ans = max(ans,val)
            else:
                val = 0
                if need+2<=idx:
                    val+= get(need+2,idx)
                s,e,g = coins[need+1]
                val+= (g*( (e+1)-max(s, y-k+1)))
                # print(val)
                ans = max(ans,val)
        return ans        