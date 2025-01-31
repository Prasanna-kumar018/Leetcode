class Solution {
    public double angleClock(int hour, int minutes) 
    {
     double z = Math.abs((double)((hour)*30)+((double)0.5*minutes)- (double)(minutes*6));
      return Math.min(z,360.0-z);
    } 

}