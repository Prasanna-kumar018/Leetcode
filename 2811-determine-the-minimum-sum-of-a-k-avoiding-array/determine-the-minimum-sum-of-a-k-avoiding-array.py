class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        start = 1
        d = set()
        total = 0
        while n>0:
            if k-start not in d:
                total+=start
                n-=1
            d.add(start)
            start+=1
        return total
