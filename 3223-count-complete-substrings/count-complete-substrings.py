class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        ans = 0
        for count in range(1, min(len(word) // k, 26) + 1):
            need = count
            L = count * k
            have = 0
            l,r = 0,0
            d = collections.defaultdict(int)
            while r<n:
                if r>0 and abs(ord(word[r])-ord(word[r-1]))>2:
                    l = r
                    have = 0
                    d = collections.defaultdict(int)
                d[word[r]]+=1
                have += 1 if d[word[r]]==k else -1 if d[word[r]]==k+1 else 0
                if r-l+1==L:
                    if have==need:
                        ans +=1
                    d[word[l]]-=1
                    have += -1 if d[word[l]]==k-1 else 1 if d[word[l]]==k else 0
                    l+=1
                r+=1
        return ans