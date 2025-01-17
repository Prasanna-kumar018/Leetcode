class Solution {
    public String largestNumber(int[] nums)
    {
     int n=nums.length;
     Integer a[]=new Integer[n];
     for(int i=0;i<n;i++)
      a[i]=nums[i];
     Arrays.sort(a,new Comparator<Integer>()
     {
        public int compare(Integer a,Integer b)
        {
            return (Integer.toString(b)+Integer.toString(a)).compareTo(Integer.toString(a)+Integer.toString(b));
        } 
     });
     StringBuilder s=new StringBuilder("");
     for(Integer i:a)
     {
        s.append(Integer.toString(i));
     }
     if( "0".repeat(s.length()).equals(s.toString()))
     return "0";
     return s.toString();
    }
}