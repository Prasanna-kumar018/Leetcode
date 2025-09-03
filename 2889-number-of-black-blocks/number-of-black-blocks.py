class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        ans = [0]*5
        # bound = [(1,1),(1,-1),(-1,1),(-1,-1)]
        # 1 2
        # 3 4
        topleft  = [(0,0),(0,-1),(-1,0),(-1,-1)]
        s = set([(x,y) for x,y in coordinates])
        #             1      2      3      4
        L = 1
        vis = set()
        total = (m-1)*(n-1)
        for x,y in coordinates:
            for dx,dy in topleft:
                cx ,cy = x+dx,y+dy
                if (cx,cy) not in vis and 0<= cx <m and 0<= cy <n and 0<= cx+L <m and 0<= cy+L <n:
                    count = 0
                    for xx in range(cx,cx+L+1):
                        for yy in range(cy,cy+L+1):
                            if (xx,yy) in s:
                                count+=1
                    ans[count]+=1
                vis.add((cx,cy))
        ans[0]=total-sum(ans)
        return ans