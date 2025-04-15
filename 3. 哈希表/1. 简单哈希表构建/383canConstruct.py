import collections


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomNote_mp = collections.Counter(ransomNote)
        magazine_mp = collections.Counter(magazine)
        for key, value in ransomNote_mp.items():
            if value > magazine_mp.get(key, 0):
                return False
        return True
