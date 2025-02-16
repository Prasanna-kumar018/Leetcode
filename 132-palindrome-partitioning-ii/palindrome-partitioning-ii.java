class Solution 
{  public int minCut(String s)
    {
        int n=s.length();
        int dp[]=new int[n];
        Arrays.fill(dp,Integer.MAX_VALUE);
        boolean isPali[][]=new boolean[n][n];
        for(int k=0;k<n;k++)
        {
            int i=0;
            int j=k;
            while(i<n && j<n)
            {
                if(j==i)
                isPali[i][j]=true;
                else if(j-i==1)
                isPali[i][j]=s.charAt(i)==s.charAt(j) ? true : false;
                else
                {
                    if(s.charAt(i)==s.charAt(j))
                    {
                        isPali[i][j]=isPali[i+1][j-1];
                    }
                }
                i++;
                j++;
            }
        }
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<=i;j++)
            {
                if(isPali[j][i])
                {
                    dp[i]=Math.min(dp[i],((j-1>=0)?dp[j-1]:0)+1);
                }
            }
        }
        return dp[n-1]-1;
    }
}