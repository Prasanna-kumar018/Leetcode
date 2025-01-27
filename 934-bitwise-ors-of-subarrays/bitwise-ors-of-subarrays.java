class Solution
 {
     public int subarrayBitwiseORs(int[] arr)
    {
        // Time Complexity --> O( 32*n );
        if( arr.length==0)
        return 0;
        int n= arr.length;
        HashSet<Integer> prev=new HashSet<>();
        HashSet<Integer> res=new HashSet<>();
        for(int i=0;i<n;i++)
        {
            HashSet<Integer> curr=new HashSet<>();
            curr.add(arr[i]);
            res.add(arr[i]);
            for(int el:prev) // this prev can be atmost 32 bits.. 
            // for example 3bits 100 010 001 
            {
                curr.add(el|arr[i]);
                res.add(el|arr[i]);
            }
           prev=curr;
        }
        return res.size();
    }
}