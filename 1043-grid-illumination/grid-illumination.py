class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        dir = [(-1,0),(1,0),(0,1),(0,-1),(-1,-1),(1,1),(-1,1),(1,-1),(0,0)]
        row = collections.defaultdict(int)
        col = collections.defaultdict(int)
        left= collections.defaultdict(int)
        right = collections.defaultdict(int)
        # for i in range(6):
        #     for j in range(6):
        #         print((n-i+j),end =' ')
        #     print()
        lamps = set([(x,y) for x,y in lamps])
        for x,y in lamps:
            row[x]+=1
            col[y]+=1
            right[(x+y)]+=1
            left[(n-x+y)]+=1
        ans = []
        # print(row,col,right,left)
        for x,y in queries:
            if row[x]>0 or col[y]>0 or right[x+y]>0 or left[n-x+y]>0:
                ans.append(1)
            else:
                ans.append(0)

            for dx,dy in dir:
                nx,ny = x+dx , y+dy
                if 0<= nx <n and 0<= ny<n and (nx,ny) in lamps:
                    lamps.discard((nx,ny))
                    row[nx]-=1
                    col[ny]-=1
                    right[nx+ny]-=1
                    left[n-nx+ny]-=1

        return ans
