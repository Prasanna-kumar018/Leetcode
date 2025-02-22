class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        INF = 10**20
        dp= [ [0 for _ in range(n)] for _ in range(n)] # count of not matched
        for k_i in range(n):
            i,j=0,k_i
            while i<n and j<n:
                if j-i==1:
                    if s[i]!=s[j]:
                        dp[i][j]=1
                elif s[i]!=s[j]:
                    val = dp[i+1][j-1] if i+1<=j-1 else 0
                    dp[i][j]=val+1
                elif s[i]==s[j]:
                    val = dp[i+1][j-1] if i+1<=j-1 else 0
                    dp[i][j]=val
                i+=1
                j+=1
        #print(dp)
        @cache
        def recur(idx,k_):
            if k_ < 0:
                return INF
            if k_==0 and idx==n:
                return 0
            best = INF
            for i in range(idx,n):
                best = min(best,recur(i+1,k_-1)+dp[idx][i])
            return best
        return recur(0,k)

        