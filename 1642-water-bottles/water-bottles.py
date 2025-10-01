class Solution:
    def numWaterBottles(self, b: int, ex: int) -> int:
        e , total = 0,0
        while b>0:
            total += b
            e += b
            aa = (e//ex)
            e %= ex
            b = aa
        return total