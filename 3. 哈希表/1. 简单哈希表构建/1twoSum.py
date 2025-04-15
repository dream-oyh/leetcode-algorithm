class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_count = {}
        for i,ele in enumerate(nums):
            if (target - ele) in nums_count:
                ans = [nums_count[target-ele], i]
                return ans
            nums_count[ele] = i

so = Solution()
so.twoSum([3,2,4],6)