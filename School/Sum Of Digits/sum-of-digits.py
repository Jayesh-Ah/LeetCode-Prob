#User function Template for python3

class Solution:
    def sumOfDigits (self, N):
        # code here
        sum = 0
        while(N>0):
            digit = N%10
            N = int(N/10)
            sum = sum + digit
        return sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.sumOfDigits(N))
# } Driver Code Ends