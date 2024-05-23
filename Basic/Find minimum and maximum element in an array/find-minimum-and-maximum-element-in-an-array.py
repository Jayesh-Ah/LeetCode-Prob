#User function Template for python3

def getMinMax(a, n):
    ans = [a[0], a[0]]
    for i in range(n):
        if (a[i] > ans[1]):
            ans[1] = a[i]
        if (a[i] < ans[0]):
            ans[0] = a[i]
    return ans
        
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        
        product = getMinMax(a, n)
        print(product[0], end=" ")
        print(product[1])

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends