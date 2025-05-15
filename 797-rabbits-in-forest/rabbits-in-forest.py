class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        s = Counter(answers)
        """
        5 5 5 5 5 5 | 5 5 5 5 5 5 

        """
        res = 0
        for key,count in s.items():
            v= count // (key+1)
            v += (1 if count%(key+1)!=0 else 0)
            res += (v*(key+1))
        return res