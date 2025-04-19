class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        combined_string = needle + "#" + haystack
        next = self.build_next(combined_string)
        for i, ele in enumerate(next):
            if ele == len(needle):
                return i - 2*len(needle)
        return -1

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

so = Solution()
print(so.strStr("sadbutsad", "sad"))
