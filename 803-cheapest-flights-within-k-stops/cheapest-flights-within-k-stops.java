import java.awt.Point;
class Solution 
{
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) 
    {
        ArrayList<Point> graph[]=new ArrayList[n];
         int  dis[]=new int[n];
         Arrays.fill(dis,Integer.MAX_VALUE);
        for(int i=0;i<n;i++)
        graph[i]=new ArrayList<>();
        for(int i=0;i<flights.length;i++)
        {
            int u=flights[i][0];
            int v=flights[i][1];
            int wt=flights[i][2];
            graph[u].add(new Point(v,wt));
        }
        Queue<Point> q=new LinkedList<>();
        int res=Integer.MAX_VALUE;
        q.add(new Point(src,0));
        dis[src]=0;
        k+=1;
        while(!q.isEmpty() && k>0)
        {
            int size=q.size();
            while(size-- >0)
            {      
                Point e= q.poll();
                for(Point p:graph[e.x])
                {
                     if(p.x==dst)
                     {
                         res=Math.min(res,e.y+p.y);
                     }
                     else  if( e.y+p.y < dis[p.x])
                     {
                        dis[p.x]=e.y+p.y;
                        q.add(new Point(p.x,e.y+p.y));
                     }
                }
            }
            k-=1;
        }
        return res==Integer.MAX_VALUE ? -1: res;
    }
}