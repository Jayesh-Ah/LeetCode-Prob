class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        maxi = float('-inf')
        ansStart, ansEnd = -1, -1
        start = -1
        for i in range(len(nums)):
            sum += nums[i]                
            if sum > maxi:
                maxi = sum
                ansStart = start
                ansEnd = i
            if sum < 0:
                sum = 0
                start = i
        return maxi   
            