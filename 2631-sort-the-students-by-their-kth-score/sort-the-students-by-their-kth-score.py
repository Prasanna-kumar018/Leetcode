class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        def s(x):
            return -x[k]

        score.sort(key=s)
        return score
