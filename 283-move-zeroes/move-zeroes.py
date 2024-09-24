class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Index of the last found non-zero element
        lastNonZeroIndex = 0
        
        # Move all non-zero elements to the front
        for current in range(len(nums)):
            if nums[current] != 0:
                # Swap only if current is not same as lastNonZeroIndex
                nums[lastNonZeroIndex], nums[current] = nums[current], nums[lastNonZeroIndex]
                lastNonZeroIndex += 1
        