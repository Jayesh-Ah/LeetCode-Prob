#User function Template for python3

class Solution:
    def modify(self, s):
        vowels=('aeiouAEIOU')
        s_list = list(s)
        i = 0
        j = len(s)-1
        while i< j:
            if s_list[i] not in vowels:
                i += 1
            elif s_list[j] not in vowels:
                j -= 1
            else:
                s_list[i], s_list[j] = s_list[j], s_list[i]
                i += 1
                j -= 1
        return "".join(s_list)
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.modify(s)
        print(ans)
# } Driver Code Ends