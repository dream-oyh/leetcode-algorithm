class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        head = 0
        rear = 0
        n = len(s)
        t_dict = self.count(t)
        s_full_dict = self.count(s)
        if not self.is_include(s_full_dict, t_dict):
            return ""
        s_dict = {s[head]: 1}
        minwindow = s
        while rear < n:
            if not self.is_include(s_dict, t_dict):
                rear += 1
                if rear >= n:
                    return minwindow
                if s[rear] not in s_dict:
                    s_dict[s[rear]] = 1
                else:
                    s_dict[s[rear]] += 1
            else:
                if len(minwindow) > (rear - head + 1):
                    minwindow = s[head : rear + 1]

                s_dict[s[head]] -= 1
                if s_dict[s[head]] == 0:
                    s_dict.pop(s[head])
                head += 1
                if head >= n:
                    return s[head - 1 : rear + 1]
        return minwindow

    def is_include(self, s_dict, t_dict):
        for i in t_dict:
            if i not in s_dict or t_dict[i] > s_dict[i]:
                return False
        return True

    def count(self, nums):
        kind_dict = {}
        for i in nums:
            if i not in kind_dict:
                kind_dict[i] = 1
            else:
                kind_dict[i] += 1
        return kind_dict


so = Solution()
print(so.minWindow("ABAACBAB", "ABC"))
