class Solution {
    
    public int findChampion(int n, int[][] edges)
    {

        int indegree[]=new int[n];
        for(int i=0;i<edges.length;i++)
        {
            indegree[edges[i][1]]=1;
        }
        int idx=-1;
        int count=0;
        for(int i=0;i<n;i++)
        {
            if(indegree[i]==0)
            {
                idx=i;
                count++;
            }
        }
        if(count>1)
        return -1;
        
      return idx;
    }
}