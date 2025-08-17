class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        """
        We can do range addition using sweep line very easily but we are going to 
        try this range addition in fenwick tree

        """
        arr = [0]*(n+1)
        for x,y,z in bookings:
            arr[x]+=z
            if y+1<=n:
                arr[y+1]-=z
        for i in range(1,n+1):
            arr[i]+=arr[i-1]
        return arr[1:]
