class Solution
{ 
    public int maxHistogram(int arr[])
    {
        int n=arr.length;
        Stack<Integer> s=new Stack();
        s.push(-1);
        int max=Integer.MIN_VALUE;
        int i = 0;
        for(i=0;i<n;i++)
        {
            while(s.size()>1 && arr[s.peek()]>arr[i])
            {
                int idx=s.pop();
                // max=Math.max(max,(idx-s.peek())*arr[idx]);  Wrong answer
                /**
                    1  2  [4 5 ] 3
                      idx        i
                 */
                max=Math.max(max,(i-s.peek()-1)*arr[idx]); 
            }
            s.push(i);
        }
        while(s.size()>1)
        {
            int idx=s.pop();
            max=Math.max(max,(i-s.peek()-1)*arr[idx]);
        }
        return max;
    }
    public int maximalRectangle(char[][] matrix) 
    {
         int m=matrix.length;
         int n=matrix[0].length;
         int arr[]= new int[n];
         Arrays.fill(arr,0);
         int max=Integer.MIN_VALUE;
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                int value=  matrix[i][j]-'0';
                if(value ==0)
                arr[j]=0;
                else
                arr[j]+=value;
            }
            max=Math.max(max,maxHistogram(arr));
        }
      return max;
    }
}