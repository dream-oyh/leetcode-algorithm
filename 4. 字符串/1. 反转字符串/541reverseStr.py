class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        s_list = list(s)
        start = 0
        num = len(s)
        while (num-start)>=k:
            
            s_list[start:start+k] = self.reverse(s_list[start:start+k])
            start += 2*k
        if num - start < k and num - start > 0:
            s_list[start:] = self.reverse(s_list[start:])
        return ''.join(s_list)

    
    def reverse(self, s):
        head = 0
        rear = len(s) - 1
        while head <= rear:
            temp = s [head]
            s[head] = s[rear]
            s[rear] = temp

            head += 1
            rear -= 1
        return s