class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)

        for ele, freq in count.items():
            if freq > len(nums)/2:
                return ele