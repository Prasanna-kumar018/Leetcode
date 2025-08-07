class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.reverse()
        q = collections.deque() # cost ,left,right
        left = 0
        ans = cost = 0
        for right,x in enumerate(nums):
            leftmost = right
            while q and q[-1][0] < x:
                val,lind,rind = q.pop()
                cost += (rind-lind+1)*(x-val)
                leftmost = lind
            q.append([x,leftmost,right])
            while cost>k:
                if q[0][2]<left:
                    q.popleft()
                y = q[0][0]
                cost -= (y-nums[left])
                q[0][1]+=1
                left+=1
            ans += (right-left+1)
        return ans