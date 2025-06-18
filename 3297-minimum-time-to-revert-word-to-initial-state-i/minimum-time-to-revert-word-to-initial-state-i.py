class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n = len(word)
        i = 0
        count = 0
        while i+k<n:
            count += 1
            if word.startswith(word[i+k:]):
                return count
            i+=k
        count+=1
        return count 