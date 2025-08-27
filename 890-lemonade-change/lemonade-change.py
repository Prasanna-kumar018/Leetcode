class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = collections.defaultdict(int)
        for x in bills:
            c = x-5
            if c>=10 and d[10]>0:
                d[10]-=1
                c-=10
            if c>=5 and d[5]>=(c//5):
                d[5]-=(c//5)
                c = 0
            if c>0:
                return False
            d[x]+=1
        return True