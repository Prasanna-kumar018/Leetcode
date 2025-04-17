import java.awt.*;
class Solution 
{
public boolean dis(Point st,Point next,int a[])
{
int dis1= (next.x - st.x)* (next.x - st.x) + (next.y - st.y)* (next.y - st.y);
int dis2= (a[0] - st.x)* (a[0] - st.x) + (a[1] - st.y)* (a[1] - st.y);
//System.out.println(dis1 +" "+dis2);
if(dis1 > dis2)
return true;
return false;
}
public int get(Point st,Point next,int a[])
{
    //cross product
int x1=next.x- st.x;
int y1=next.y-st.y;
int x2=a[0]-st.x;
int y2=a[1]-st.y;

return (y2*x1)-(y1*x2);
}

public int[][] outerTrees(int[][] trees) 
{
int n=trees.length;
Arrays.sort(trees,new Comparator<int []>()
{
public int compare(int a[],int b[])
{
    if(a[0]!=b[0])
     return a[0]-b[0];
  return a[1]-b[1];  // to get the bottom left point...
}
});
//System.out.println(Arrays.deepToString(trees));
HashSet<Point> h=new HashSet<>();
Point start = new Point(trees[0][0],trees[0][1]);
h.add(start);
Point curr=new Point(start.x,start.y);
while(true)
{
Point nextTarget= new Point(curr.x,curr.y);;
HashSet<Point> colli= new HashSet<>();
for(int i=0;i<n;i++)
{
if(curr.equals(new Point(trees[i][0],trees[i][1])))
continue;
int value= get(curr,nextTarget,trees[i]);
if(value>0)
{
nextTarget=new Point(trees[i][0],trees[i][1]);
colli.clear();
}
else if(value ==0)
{
if(dis(curr,nextTarget,trees[i]))
{
colli.add(new Point(trees[i][0],trees[i][1]));
}
else
{
colli.add(nextTarget);
nextTarget=new Point(trees[i][0],trees[i][1]);
}
}

}
//System.out.println(colli.toString() +" "+ nextTarget.toString());
for(Point s:colli)
h.add(s);

h.add(nextTarget);

curr=nextTarget;
//System.out.println(h.toString());
if(nextTarget.equals(start))
break;
}
int res[][]=new int[h.size()][2];
int i=0;
for(Point s:h)
{
res[i][0]=s.x;
res[i][1]=s.y;
i++;
}
return res;
}
}