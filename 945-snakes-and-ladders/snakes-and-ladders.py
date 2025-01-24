class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        q = [1]
        vis = set()
        n = len(board)
        ans = 0
        while len(q)>0:
            size = len(q)
            while size>0:
                val = q.pop(0)
                if val not in vis:
                    vis.add(val)
                    if val==n*n:
                        return ans
                    for i in range(val+1,min(val+6,n*n)+1):
                        x = n-1-((i-1)//n)
                        y = (i-1)%n
                        if (n-1-x)%2==1:
                            y= (n-1)-y
                        res = board[x][y] if board[x][y]!=-1 else i
                        if res not in vis:
                            q.append(res)
                        
                size-=1
            ans+=1
        return -1