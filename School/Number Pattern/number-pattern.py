#User function Template for python3
class Solution:
    def numberPattern(self, N):
        ans = []
        for i in range(1, N + 1):
            first_part = ''.join(str(j) for j in range(1, i + 1))
            second_part = ''.join(str(j) for j in range(i - 1, 0, -1))
            line = first_part + second_part
            ans.append(line)
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        ob = Solution()
        res = ob.numberPattern(N)
        for each in res:
            print(each, end=" ")
        print()
        

# } Driver Code Ends