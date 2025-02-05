class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        need = len(set(nums))
        def atmost(k):
            n = len(nums)
            l,r = 0,0
            vis = collections.defaultdict(int)
            res = 0
            while r<n:
                vis[nums[r]]+=1
                while len(vis)>k and l<=r:
                    vis[nums[l]]-=1
                    if vis[nums[l]]==0:
                        del vis[nums[l]]
                    l+=1
                res += (r-l+1)
                r+=1
            return res
        return atmost(need)-atmost(need-1)
                