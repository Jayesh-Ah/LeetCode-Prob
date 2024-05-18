#User function Template for python3

class Solution:
    def mean(self, N , A):
        sum = 0
        for i in range(0,N):
            sum += A[i]
        mean = sum // N
        return  mean


#{
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        A = list(map(int,input().split()))
        
        ob = Solution()
        print(ob.mean(N,A))
# } Driver Code Ends