class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        neg = 0
        for i, num in enumerate(nums):
            if num < 0:
                neg = i
            else:
                pass
        pos = neg + 1
        ans = []

        def square(num):
            return num**2

        while neg >= 0 and pos <= (len(nums) - 1):
            if square(nums[pos]) < square(nums[neg]):
                ans.append(square(nums[pos]))
                pos += 1
            elif square(nums[pos]) >= square(nums[neg]):
                ans.append(square(nums[neg]))
                neg -= 1
        if neg < 0:
            while pos <= (len(nums) - 1):
                ans.append(square(nums[pos]))
                pos += 1
        elif pos > (len(nums) - 1):
            while neg >= 0:
                ans.append(square(nums[neg]))
                neg -= 1
        return ans

