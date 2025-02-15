class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        s = [str(i) for i in range(1,n+1)]
        per = []
        for x in permutations(s):
            per.append(''.join(x))
        return per[k-1]
        