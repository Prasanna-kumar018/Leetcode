/*
// Definition for a QuadTree node.
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;

    
    public Node() {
        this.val = false;
        this.isLeaf = false;
        this.topLeft = null;
        this.topRight = null;
        this.bottomLeft = null;
        this.bottomRight = null;
    }
    
    public Node(boolean val, boolean isLeaf) {
        this.val = val;
        this.isLeaf = isLeaf;
        this.topLeft = null;
        this.topRight = null;
        this.bottomLeft = null;
        this.bottomRight = null;
    }
    
    public Node(boolean val, boolean isLeaf, Node topLeft, Node topRight, Node bottomLeft, Node bottomRight) {
        this.val = val;
        this.isLeaf = isLeaf;
        this.topLeft = topLeft;
        this.topRight = topRight;
        this.bottomLeft = bottomLeft;
        this.bottomRight = bottomRight;
    }
};
*/

class Solution {
    public Node cons(int [][]grid,int istart,int jstart
    ,int iend,int jend)
    { 
         if(check(istart,jstart,iend,jend,grid,grid[istart][jstart]))
         {
            Node t=new Node();
            t.val=(grid[istart][jstart]==1);
            t.isLeaf=true;
            return t;
         }
         Node node =new Node();
         int ilen = (iend-istart+1)/2;
         int jlen = (jend-jstart+1)/2;
          node.topLeft=cons(grid,istart,jstart,
            istart+ilen-1,jstart+jlen-1);  
              node.topRight=cons(grid,istart,
              jstart+jlen,
              istart+ilen-1,jend);
               node.bottomLeft=cons(grid,
               istart+ilen,jstart,
               iend,jstart+jlen-1);
               node.bottomRight=cons(grid,istart+ilen,
                jstart+jlen,iend,jend ); 
          return node;
    }  
    public boolean check(int i,int j,int m,int n,int grid[][],int value)
    {
        for(int q=i;q<=m;q++)
        {
            for(int w=j;w<=n;w++)
            {
                if(grid[q][w]!=value)
                 {
                    return false;
                 }

            }
        }
        return true;       
    }
    public Node construct(int[][] grid) 
    {
       return cons(grid,0,0,grid.length-1,grid[0].length-1);         
    }
}