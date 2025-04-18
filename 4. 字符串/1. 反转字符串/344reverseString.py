class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        head = 0
        rear = len(s) - 1
        while head <= rear:
            temp = s [head]
            s[head] = s[rear]
            s[rear] = temp

            head += 1
            rear -= 1
        return s