class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        indexed_nums.sort(key=lambda x: x[0])
        i, j = 0, len(nums)-1 
        while i < j:
            if indexed_nums[i][0] + indexed_nums[j][0] == target:
                return[indexed_nums[i][1], indexed_nums[j][1]]
            elif indexed_nums[i][0] + indexed_nums[j][0] < target:
                i+=1
            else:
                j-=1
