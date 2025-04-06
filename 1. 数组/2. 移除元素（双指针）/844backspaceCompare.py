class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        s = self.backstep(s)
        t = self.backstep(t)
        return s == t

    def backstep(self, s):
        s_fast = 0
        s_slow = -1
        s = list(s)
        for i in range(len(s)):
            if s[s_fast] != "#":
                s_slow += 1
                s[s_slow] = s[s_fast]
            elif s[s_fast] == "#":
                if s_slow > -1:
                    s_slow -= 1
                else:
                    s_slow = -1
            s_fast += 1
        if s_slow == -1:
            return ""
        else:
            return "".join(s[0:s_slow+1])