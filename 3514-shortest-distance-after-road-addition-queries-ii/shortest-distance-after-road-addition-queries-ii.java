class Solution {
    public int[] shortestDistanceAfterQueries(int n, int[][] queries) {
        TreeSet<Integer> t= new TreeSet<>();
        for(int i=0;i<n;i++)
        t.add(i);
        int i=0;
        n = queries.length;
        int res []=new int[n];
        for(int k[]:queries)
        {
            int start= k[0]+1;
            int end = k[1]-1;
            if(start<=end)
            {
                t.subSet(start,true,end,true).clear();
            }
            res[i]=t.size()-1;
            i+=1;
        }
        return res;
    }
}