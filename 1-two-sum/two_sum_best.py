class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        count = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in count:
                return [count[diff], i]
            count[nums[i]] = i
