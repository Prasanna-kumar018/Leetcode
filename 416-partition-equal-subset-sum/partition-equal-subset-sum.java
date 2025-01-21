class Solution {
    public boolean canPartition(int[] nums) 
    {
        int n=nums.length;
        int sum= Arrays.stream(nums).sum();
        if(sum%2==1)
        return false;
        sum/=2;
        boolean res[][]=new boolean[n][sum+1];
        for(int i=0;i<n;i++)
        res[i][0]=true;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<=sum;j++)
            {
                if(i==0)
                {
                    if(j-nums[i]==0)
                    res[i][j]=true;
                }
                else if (j>=nums[i])
                {
                   
                    res[i][j]= res[i-1][j] || res[i-1][j-nums[i]];
                }
                else
                res[i][j]=res[i-1][j];
            }
        }
    //   System.out.println(Arrays.deepToString(res));
        return res[n-1][sum];
    }
}