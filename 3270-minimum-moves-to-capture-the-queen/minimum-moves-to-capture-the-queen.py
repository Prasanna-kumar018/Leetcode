class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        def isgreater(bis,rook,queen):
            dis1 = (rook[0]-bis[0])**2 + (rook[1]-bis[1])**2
            dis2 = (queen[0]-bis[0])**2 + (queen[1]-bis[1])**2
            # print(dis1,dis2)
            if dis1>dis2:
                return True
            return False
        # 1 or 2 could be the answer
        # rook
        if (a==e or b==f):
            if math.atan2(f-b,e-a)==math.atan2(d-b,c-a):
                if isgreater((a,b),(c,d),(e,f)):
                    return 1
            else:
                return 1
        # bishop
        if math.atan2(b-d,a-c)!=math.atan2(f-d,e-c):
            if abs(e-c)==abs(d-f):
                return 1
        else:
            if isgreater((c,d),(a,b),(e,f)):
                return 1
        return 2