class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        vis=set()
        m=len(board)
        n=len(board[0])
        count=0
        dir = [(-1,0),(1,0),(0,1),(0,-1)]
        def dfs(i,j):
            if board[i][j]=='.':
                return
            board[i][j]='.'
            for x,y in dir:
                nx = x+i
                ny = y+j
                if 0<=nx < m and 0<= ny <n:
                    dfs(nx,ny)
        for i in range(m):
            for j in range(n):
                if board[i][j]=='X':
                    dfs(i,j)
                    count+=1
        return count
        