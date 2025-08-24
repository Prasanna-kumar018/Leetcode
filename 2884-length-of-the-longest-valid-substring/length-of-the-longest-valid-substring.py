class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        f = set(forbidden)
        N = len(word)
        MAXI = 10
        def bad():
            M = len(curr)
            w = ""
            for i in range(M-1,-1,-1):
                if M-i>MAXI:
                    break
                w = curr[i] + w
                if w in f:
                    return True
            return False
        ans = 0
        curr = collections.deque()
        for r in range(N):
            curr.append(word[r])
            while bad():
                curr.popleft()
            ans = max(ans,len(curr))
        return ans