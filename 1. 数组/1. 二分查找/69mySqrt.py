class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x
        while left<=right:
            mid = (left+right)//2
            if mid**2 > x:
                right = mid - 1
            elif mid**2 < x:
                left = mid + 1
            elif mid**2 == x:
                return mid
        return left-1