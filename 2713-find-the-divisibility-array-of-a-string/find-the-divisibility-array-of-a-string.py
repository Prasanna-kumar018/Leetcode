class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        n = len(word)
        res = []
        val = 0
        for x in word:
            x = int(x)
            val = val*10 + x
            val %= m
            if val==0:
                res.append(1)
            else:
                res.append(0)
        return res 