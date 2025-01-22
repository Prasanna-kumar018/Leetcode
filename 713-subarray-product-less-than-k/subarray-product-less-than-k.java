class Solution 
{
    public int numSubarrayProductLessThanK(int[] nums, int k)
    {
        if(k==0)
        return 0;
        int n=nums.length;
        int l=0,r=0;
        int prod=1;
        int c=0;
        while(r<n)
        {
            prod*=nums[r];
            r++;
            while(prod>=k && l<r)
            {
                prod/=nums[l];
                l++;
            }
            c+=(r-l);
        }
        return c;
    }
}