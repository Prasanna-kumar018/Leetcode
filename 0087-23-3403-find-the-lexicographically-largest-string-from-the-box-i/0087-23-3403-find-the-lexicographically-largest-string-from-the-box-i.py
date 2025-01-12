class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends ==1:
            return word
        n = len(word)-(numFriends-1)
        x = len(word)
        ans = ''
        for i in range(x):
            res = word[i:min(i+n,x)]
            # print(res,ans)
            if res > ans:
                ans = res
        return ans