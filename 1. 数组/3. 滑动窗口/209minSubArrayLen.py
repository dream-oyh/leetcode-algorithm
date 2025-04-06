class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        head = 0
        rear = 0
        sum = 0
        sublength = float('inf')
        while rear < n:
            sum += nums[rear]

            while sum >= target:
                sublength = min(rear - head + 1, sublength)
                sum -= nums[head]
                head += 1

            rear += 1
        return sublength if sublength != float('inf') else 0

so = Solution()
print(so.minSubArrayLen(7,[2,3,1,2,4,3]))