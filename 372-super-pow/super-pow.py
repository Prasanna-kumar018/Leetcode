class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        x = list(map(str,b))
        return pow(a,int(''.join(x)),1337)