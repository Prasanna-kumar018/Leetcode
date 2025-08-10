class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        """
        pow(anything , -1 , MOD) works only if the MOD is prime 
        here 12345 is not prime . So it does not work


        It is similar to product of array except self....  
        """
        prod = 1
        MOD = 12345
        M = len(grid)
        N = len(grid[0])
        ans =[ [0]*N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                ans[i][j]=prod
                prod *= grid[i][j]
                prod %= MOD
        prod = 1
        for i in range(M-1,-1,-1):
            for j in range(N-1,-1,-1):
                ans[i][j]*=prod
                prod *= grid[i][j]
                prod %= MOD
                ans[i][j]%=MOD
        return ans 