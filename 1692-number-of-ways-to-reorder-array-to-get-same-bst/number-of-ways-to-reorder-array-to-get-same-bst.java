class Solution {
    long mod = (long)Math.pow(10,9)+(long) 7;
    long ncr[][]=new long[1000][1000];
    public long  recur (List<Integer> nums)
    {
            if (nums.size() <=1)
                return 1;
            List<Integer> l=new ArrayList<>();
            List<Integer> r=new ArrayList<>();
            for(int i=1;i<nums.size();i++)
            {
                if(nums.get(i) < nums.get(0))
                  l.add(nums.get(i));
                else 
                   r.add(nums.get(i));
            }
            int left = l.size();
            int right =r.size();
            // return (ncr[left+right][left]*(recur(l)*(recur(r))%mod))%mod;
            return (ncr[left+right][right]*(recur(l)*(recur(r))%mod))%mod;
    }
    public int numOfWays(int[] nums) 
    {
      for (int n = 0; n < 1000; n++) {
            for (int r = 0; r <= n; r++) {
                if (r == 0 || n==0 ) 
                {
                    ncr[n][r] = 1;
                    continue;
                }
                ncr[n][r] = (ncr[n - 1][r - 1] + ncr[n - 1][r]) % mod;
                
            }
        }
        List<Integer> n=Arrays.stream(nums).boxed().collect(Collectors.toList());
        return (int)recur(n)-1;
    }
}