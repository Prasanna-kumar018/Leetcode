class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dir = [(-1,0),(1,0),(0,1),(0,-1)]
        # 200*200*4*4
        @cache
        def go(x,y,parx,pary):
            res = 0
            for dx,dy in dir:
                nx,ny = x+dx,y+dy
                if 0<= nx < m and 0<= ny < n and matrix[nx][ny]>matrix[x][y]:
                    res = max(res,go(nx,ny,x,y)+1)
            return res
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans,go(i,j,-1,-1)+1)
        return ans