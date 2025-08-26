class Solution {
    public boolean ex(char [][]board,String word,int i,int j,int idx)
    {
        if(word.charAt(idx)!=board[i][j] || board[i][j]=='$')
        return false;
       if(idx==word.length()-1)
        return true;
        char c=board[i][j];
        board[i][j]='$';
        if(i>0 && ex(board,word,i-1,j,idx+1))
        return true;
        if(j>0 && ex(board,word,i,j-1,idx+1))
              return true;
        if(i<board.length-1 && ex(board,word,i+1,j,idx+1))
           return true;
        if(j<board[0].length-1 && ex(board,word,i,j+1,idx+1))
            return true;
        board[i][j]=c;
      return false;
    }
    public boolean exist(char[][] board, String word) 
    {
        for(int i=0;i<board.length;i++)
        {
            for(int j=0;j<board[0].length;j++)
             {
               if(board[i][j]==word.charAt(0))
                 {
                 if(ex(board,word,i,j,0))
                 return true;        
                 }
                 
             }
        }
        return false;
        }
    }
