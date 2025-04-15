class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow = n
        fast = n
        while True:

            slow = self.bitSquare(slow)
            fast = self.bitSquare(fast)
            fast = self.bitSquare(fast)
            if slow == fast:
                break
        return slow == 1

    def bitSquare(self, n):
        n_list = str(n)
        sum = 0
        for i in n_list:
            sum += int(i) ** 2
        return sum
