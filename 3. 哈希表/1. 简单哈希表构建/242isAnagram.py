import collections
class Solution1(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_count = {}
        t_count = {}

        for i in s:
            if i not in s_count:
                s_count[i] = 1
            else:
                s_count[i] += 1

        for j in t:
            if j not in t_count:
                t_count[j] = 1
            else:
                t_count[j] += 1
        return s_count == t_count


class Solution2(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return True if collections.Counter(s) == collections.Counter(t) else False