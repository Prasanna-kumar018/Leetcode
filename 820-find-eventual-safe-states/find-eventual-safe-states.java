class Solution 
{
    
    public List<Integer> eventualSafeNodes(int[][] graph)
    {
        ArrayList<Integer>  arr[]=new ArrayList[graph.length];
         int outdegree[]=new int[graph.length]; 
         Queue<Integer> q=new LinkedList<>();
         List<Integer> l=new ArrayList<>();
         for(int i=0;i<graph.length;i++)
           arr[i]=new ArrayList<>();
         for(int i=0;i<graph.length;i++)
         {
                for(int v:graph[i])
                {
                   arr[v].add(i);
                }
                outdegree[i]=graph[i].length;
             if(outdegree[i]==0)
             q.add(i);           
        }
        while(!q.isEmpty())
        {
            int x=q.poll();
            l.add(x);
            for(int v:arr[x])
            {
                outdegree[v]--;
                if(outdegree[v]==0)
                q.add(v);
            }
        }
        Collections.sort(l);
        return l;
    }
}