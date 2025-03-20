class Solution 
{
    public void floydWarshall(int mat[][],int n)
    {
         for(int i=0;i<n;i++)
         {
           for(int j=0;j<n;j++)
           {
               for(int k=0;k<n;k++)
               {
                if(mat[j][i]!=Integer.MAX_VALUE && mat[i][k]!=Integer.MAX_VALUE )
                    mat[j][k]=Math.min(mat[j][k],mat[j][i]+mat[i][k]);
               }
           }
         }
    }
    public int numberOfSets(int n, int max, int[][] roads)
    { 
        HashSet<Integer>  comb[]=new HashSet[(int)Math.pow(2,n)];
        HashSet<Integer> h=new HashSet<>();
        int arr[]=new int[n];
        int graph[][]=new int[n][n];
        int ans=0;
        for(int k[]:graph)
        {
            Arrays.fill(k,Integer.MAX_VALUE);
        }
        for(int i=0;i<(int)Math.pow(2,n);i++)
        {
            boolean b=true;
            int j=arr.length-1;
            comb[i]= new HashSet<>(h);
            while(b && j>=0)
            {
                if(arr[j]==0)
                    b=false;
                if(arr[j]==1)
                {
                   arr[j]=0;
                    h.remove(j);
                }
                else 
                {
                    arr[j]=1;
                    h.add(j);
                }
                j--;
            }
        }
        for(int k[]:roads)
        {
            graph[k[0]][k[1]]=Math.min(k[2],graph[k[0]][k[1]]);
            graph[k[1]][k[0]]=Math.min(k[2],graph[k[1]][k[0]]);
        }
        for(HashSet<Integer> H:comb)
        {
           //System.out.println(H.toString());
           int mat[][]=new int[n][n];
           for(int i=0;i<n;i++)
           {
               for(int j=0;j<n;++j)
               {
                   mat[i][j]=graph[i][j];
               }
           }
           for(Integer i:H)
           {
                for(int j=0;j<n;j++)
                {
                    mat[i][j]=Integer.MAX_VALUE;
                    mat[j][i]=Integer.MAX_VALUE;
                }
           }
           floydWarshall(mat,n);
          //  for(int k[]:mat)
            //System.out.println(Arrays.toString(k));
           boolean d=true;
           for(int i=0;i<n;i++)
           {
                if(H.contains(i))
                   continue;
               for(int j=0;j<n;j++)
               {
                   if( i!=j && !H.contains(i) && !H.contains(j))
                   {
                       if(mat[i][j]>max )
                       {
                          d=false;
                       }
                   }
               }        
            }
            if(d)
            {
            //    System.out.println( "-???" + H.toString() +   "->>>" );
                ans++;
                
            }
        }
   //     System.out.println();
        return ans;
        
    }
}