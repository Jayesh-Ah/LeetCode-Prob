#User function Template for python3

class Solution:
    def nthTermOfAP(self,A1,A2,N):
        #code here
        d = A2 - A1
        A = A1 + (N-1)*d
        return A


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        A1,A2,N=map(int,input().strip().split(' '))
        ob=Solution()
        print(ob.nthTermOfAP(A1,A2,N))  
# } Driver Code Ends