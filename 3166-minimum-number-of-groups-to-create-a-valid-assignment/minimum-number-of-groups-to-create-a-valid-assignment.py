class Solution:
    def minGroupsForValidAssignment(self, balls: List[int]) -> int:
        d=collections.Counter(balls)
        INF = 10**10
        def good(i):

            for x in d.values():
                l = x//i 
                g = x % i # if g > l then it wont be divided into target and
                # target+1 .Here i is the target
                if g>l:
                    return False
            return True
        def calc(i):
            group = 0
            for x in d.values():
                l2 = x%(i+1)
                g2 = x//(i+1)
                if l2>0:
                    g2+=1
                group+= g2
            return group
        mini = min(d.values())
        best = INF
        for i in range(1,mini+1):
            if good(i):
                best = min(best,calc(i))
        return best