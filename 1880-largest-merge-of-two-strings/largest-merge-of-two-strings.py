class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        w1 = deque(word1)
        w2 = deque(word2)
        res = []
        while w1 or  w2:
            if w1<w2:
                res.append(w2.popleft())
            else:
                res.append(w1.popleft())
        return ''.join(res)