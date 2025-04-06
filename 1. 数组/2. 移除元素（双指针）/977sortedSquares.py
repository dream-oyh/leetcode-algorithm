class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        head = 0
        rear = len(nums) - 1
        ans = []
        while head <= rear:
            if nums[head] ** 2 > nums[rear] ** 2:
                ans.append(nums[head] ** 2)
                head += 1
            elif nums[head]**2 < nums[rear] ** 2:
                ans.append(nums[rear] ** 2)
                rear -= 1
            else:
                ans.append(nums[head] ** 2)
                head += 1

        return ans[::-1]

solution = Solution()
print(solution.sortedSquares([-4,-1,0,3,10]))