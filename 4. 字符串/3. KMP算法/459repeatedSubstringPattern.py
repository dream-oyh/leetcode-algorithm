class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 1:
            return False
        next = self.build_next(s)
        i = len(s)
        if next[-1] != 0 and i % (i - next[-1]) == 0:
            return True
        else:
            return False

    def build_next(self, s):
        next = [0]
        for i in range(1, len(s)):
            pre_len = next[i - 1]

            while pre_len > 0 and s[pre_len] != s[i]:
                pre_len = next[pre_len - 1]

            if s[pre_len] == s[i]:
                pre_len += 1
            next.append(pre_len)
        return next


solution = Solution()

solution.repeatedSubstringPattern("abaababaab")
