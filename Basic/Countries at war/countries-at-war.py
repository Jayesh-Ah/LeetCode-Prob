#User function Template for python3

def Country_at_war (arr, brr, n) : 
    acount, bcount = 0, 0
    for i in range(n):
        if(arr[i]>brr[i]):
            acount += 1
        if(arr[i]<brr[i]):
            bcount += 1
    if(acount>bcount):
        return("A")
    elif(acount<bcount):
        return("B")
    else:
        return("DRAW")



#{ 
 # Driver Code Starts
#Initial Template for Python 3

    
for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    brr = list(map(int, input().strip().split()))
    ans = Country_at_war(arr, brr, n)
    print(ans)
    





# } Driver Code Ends