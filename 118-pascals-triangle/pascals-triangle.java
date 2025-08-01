class Solution {
    public List<List<Integer>> generate(int numRows) 
    {
        List<List<Integer>> li=new ArrayList<>();
        for(int n=0;n<numRows;n++)
        {
            List<Integer> l=new ArrayList<>();
            int ncr=0;
            for(int r=0;r<=n;r++)
            {
              if(r==0)
              { ncr=1;
                l.add(ncr);
              }
              else
              {
                  ncr=ncr*(n-r+1)/r;
                  l.add(ncr);
              }
            }
            li.add(l);
        }    
        return li;
    }
}