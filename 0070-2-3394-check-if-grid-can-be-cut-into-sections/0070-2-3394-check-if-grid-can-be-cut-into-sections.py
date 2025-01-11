class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        m ,n =0,0 
        # [startx, starty, endx, endy],
        xs ,ys = collections.defaultdict(int) , collections.defaultdict(int)
        for x,y, a,b in rectangles:
            x*=2
            y*=2
            a*=2
            b*=2
            xs[a-1]+=1
            xs[x+1]-=1
            ys[b-1]+=1
            ys[y+1]-=1
        # print(xs,ys)
        def good(xs):
            maxi = max(xs)
            count = 0
            c =0
            for x in sorted(xs.keys(),reverse=True):
                count += xs[x]
                # print(x,xs,count)
                if count ==0:
                    c+=1
            return c>=3
        return good(xs) or good(ys)
        
        
            