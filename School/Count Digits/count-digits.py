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

#METHOD 2
def count_divisible_digits(N):
    # Convert the number to a string to iterate through its digits
    N_str = str(N)
    
    # Initialize a counter for divisible digits
    count = 0
    
    # Iterate through each digit in the number
    for digit_str in N_str:
        # Convert the digit back to an integer
        digit = int(digit_str)
        
        # Check if the digit is not zero and evenly divides N
        if digit != 0 and N % digit == 0:
            count += 1
    
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
