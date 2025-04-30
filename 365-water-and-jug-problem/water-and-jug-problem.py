class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        g = gcd(x,y)
        if x+y<target:
            return False
        """
        According to Bézout's identity:
        if we want to find the gcd(a,b) then that would be equal to 
        gcd(a,b) = ax+by where x and y can be any integer...

        if x==0 we use only b
        if y==0 we use only a

        gcd(a,b)  generate some integer value of x and y

        we have to check whether that value is equal to target
        """
        return target%g ==0