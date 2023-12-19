#User function Template for python3


class Solution:
    def evenlyDivides (self, N):
        # code here
        num = int(N)
        count = 0
        while num>0:
            digit = num % 10
            if(digit != 0 and N % digit == 0):
                count += 1
            num = int(num/10)
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends