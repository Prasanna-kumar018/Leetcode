class Solution {
    public int compress(char[] chars) 
    {
        int n=chars.length;
        if(n==1) return 1;
       String s = String.valueOf(chars);
       String arr [] = s.split("(?<=(.))(?!\\1)");
       int c=0;
       int idx=0;
    //    System.out.println(Arrays.toString(arr));
       for(int i=0;i<arr.length;i++)
       {
           String a=arr[i];
           idx+=1;
           chars[idx-1]=a.charAt(0);
           c=Integer.toString(a.length()).length();
        //    System.out.println(c);
           if(a.length()>1)
           {
              for(char w:Integer.toString(a.length()).toCharArray())
              {
                idx+=1;
                chars[idx-1]=w;
              }
           }
       }    
       return idx;
    }
}