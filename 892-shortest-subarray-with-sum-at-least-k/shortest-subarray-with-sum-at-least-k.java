class Solution {
    public int shortestSubarray(int[] nums, int k) {
       TreeMap<Long,Integer> t = new TreeMap<>();
       int n = nums.length;
       t.put(0l,-1);
       int res = Integer.MAX_VALUE;
       long s = 0;
       for(int i=0;i<n;i++)
       {
         int x= nums[i];
         s+=x;
         long target = s-k;
         while( !t.isEmpty() && t.firstKey()<=target)
         {
             int idx = t.get(t.firstKey());
             res = Math.min(res,i-idx);
             t.remove(t.firstKey());
         }
         t.put(s,i);
       }  
       return res!=Integer.MAX_VALUE ? res :-1 ;
    }
}