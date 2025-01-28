class Solution {
    public int[] prisonAfterNDays(int[] cells, int n) 
    {
        int cells2[]=new int[8];
      for(int i=1;i<7;i++)
       {
           if(cells[i-1]==cells[i+1])
              cells2[i]=1;
           else 
             cells2[i]=0;
       } 
       cells=cells2.clone();
      n = (n-1) % 14;
    for(int j=0;j<n;j++)
    {
       for(int i=1;i<7;i++)
       {
           if(cells[i-1]==cells[i+1])
               cells2[i]=1;
           else 
              cells2[i]=0;
       } 
        cells=Arrays.copyOf(cells2,8);
     }
      return cells;   
    }

}