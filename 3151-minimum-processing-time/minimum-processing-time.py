class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        n = len(processorTime)
        ans = 0
        for i,val in enumerate(processorTime):
            j = 0
            while j<4:
                ans = max(ans,tasks[4*i+j]+val)
                j+=1
        return ans