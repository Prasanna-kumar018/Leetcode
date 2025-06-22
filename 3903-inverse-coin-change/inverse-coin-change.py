class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:
        ans = []
        numWays = [1] + numWays
        N = len(numWays)
        while True:
            r = -1
            try:
                r = numWays.index(1,1)
            except:
                if sum(numWays) == 1:
                    return ans
                return []
            ans.append(r)
            for idx in range(N-1,-1,-1):
                if idx-r>=0:
                    if numWays[idx-r]>0:
                        if numWays[idx]>=numWays[idx-r]:
                            numWays[idx]-=numWays[idx-r]
                        else:
                            return []
        return ans