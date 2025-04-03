class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)
        while left < right:
            middle = (left+right)//2
            if target>nums[middle]:
                left = middle + 1
            elif target<nums[middle]:
                right = middle
            elif target == nums[middle]:
                return middle
        return -1
