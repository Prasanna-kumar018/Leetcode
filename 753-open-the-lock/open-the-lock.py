class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q = collections.deque([target])
        n = 4
        deadends = set(deadends) 
        level = 0   
        while q:
            s = len(q)
            while s>0:
                a = q.popleft()
                if a == '0000':
                    return level
                # print(' ds'fgesr',a)
                for i in range(n):
                    x = list(map(int,a))
                    x[i]= (x[i]+1)%10
                    # print(''.join(map(str,x)))
                    if ''.join(map(str,x)) not in deadends:
                        q.append(''.join(list(map(str,x))))
                        deadends.add(''.join(list(map(str,x))))
                    x = list(map(int,a))
                    x[i]= (x[i]-1)%10
                    # print(''.join(map(str,x)))
                    if ''.join(map(str,x)) not in deadends:
                        q.append(''.join(list(map(str,x))))
                        deadends.add(''.join(list(map(str,x))))
                s-=1
            # print(q)
            level+=1
        return -1