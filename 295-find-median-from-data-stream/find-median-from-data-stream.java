class MedianFinder
{

    PriorityQueue<Integer> min;
    PriorityQueue<Integer> max;
    public MedianFinder() 
    {
         min=new PriorityQueue<>();
         max=new PriorityQueue<>(Comparator.reverseOrder());
    }
    
    public void addNum(int num)
    {
        max.add(num);
        if( !max.isEmpty()  && !min.isEmpty() &&  max.peek()>min.peek())
        {
            min.add(max.poll());
        }
       if( max.size()>min.size()+1)
       {
           min.add(max.poll());
       }  
       if(min.size()> max.size()+1)
       {
        max.add(min.poll());
       }      
    }
    
    public double findMedian() {
        if(min.size()> max.size())
        return min.peek();
        else if(max.size() > min.size())
        return max.peek();
        else
        return (double)(max.peek()+min.peek())/(double)2;
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */