class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        n = len(answers)
        res = n
        for x,y in Counter(answers).items():
            v = (x+1)
            c = y % v
            if c>0:
                c = (v -c)
            res += c
        return res