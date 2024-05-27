#User function template for Python

class Solution:	
	def binarysearch(self, arr, n, k):
	    lo = 0
	    hi = n-1
	    ans = -1
		while lo <= hi:
		    mid = (hi+lo)//2
		    if arr[mid]==k:
		        ans = mid
		        break
		    if arr[mid]>k:
		        hi = mid-1
		    if arr[mid]<k:
		        lo = mid+1
		return ans
		        


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int, input().strip().split(' ')))
        k=int(input())
        ob = Solution()
        print (ob.binarysearch(arr, n, k))


# } Driver Code Ends