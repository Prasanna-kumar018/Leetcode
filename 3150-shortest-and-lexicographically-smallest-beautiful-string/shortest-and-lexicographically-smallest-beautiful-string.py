class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        INF = 10**20
        ans  = '' # For empty String (not ans)  would return True
        ones = 0
        q = collections.deque()
        r = 0
        while r<n:
            if s[r]=='1':
                ones+=1
            q.append(s[r])
            while q and ones>k:
                if q[0]=='1':
                    ones-=1
                q.popleft()
            while q and q[0]=='0':
                q.popleft()
            if ones==k:
                ss = ''.join(list(q))
                # print(ss)
                if not ans:
                    ans = ss
                elif len(ans) > len(ss):
                    ans = ss
                elif len(ans)==len(ss) and ss < ans:
                    ans = ss

            r+=1
        # print(ans)
        return ans 