#User function Template for python3
class Solution:
    def pattern(self, S):
        # code here
        l=len(S)
        k=[]
        for i in range(len(S)):
            S=S[0:l]
            k.append(S)
            l-=1
        return k



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.pattern(S)
		for value in answer:
			print(value)
			

# } Driver Code Ends