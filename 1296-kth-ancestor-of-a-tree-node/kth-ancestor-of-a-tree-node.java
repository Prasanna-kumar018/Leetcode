class TreeAncestor 
{
    int up[][];
    int log;
    public TreeAncestor(int n, int[] parent)
    {
      int log=(int)(Math.log(n)/Math.log(2))+1;
      up=new int[log][n];
      for(int u[]:up)
      Arrays.fill(u,-1);
      up[0]=parent;
    for(int i=1;i<log;i++)
    {
      for(int j=0;j<n;j++)
      {
          int x=up[i-1][j];
          if(x!=-1)
          up[i][j]=up[i-1][x];   
      }
    }
   // for(int u[]:up)
    //System.out.println(Arrays.toString(u));
    }    
    public int getKthAncestor(int node, int k)
    {

     for(int i=0;i<32;i++)
     {
        if( ((k&(1<<i))!=0 ) && node!=-1)
        {
            node=up[i][node];
        }     
     }
     return node;
    }
}

/** Your TreeAncestor object will be instantiated and called as such:
 TreeAncestor obj = new TreeAncestor(n, parent);
 int param_1 = obj.getKthAncestor(node,k);
 */