class Solution 
{
    public String removeKdigits(String num, int k) 
    { 
        Stack<Character> s=new Stack<>();
        for(char c:num.toCharArray())
        {
            while(!s.isEmpty() && k>0 && s.peek()>c)
            {
                s.pop();
                k-=1;
            }
            if(!s.isEmpty())
            s.push(c);
            else if(c!='0')
            s.push(c);
        }
        while(!s.isEmpty() && k>0)
        {
        k--;
        s.pop();
        }
        StringBuilder res=new StringBuilder();
        while(!s.isEmpty())
         res.insert(0,s.pop());
        if(res.length()==0)
        return "0";
    return res.toString();
    }
}