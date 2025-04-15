class Solution1(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s1_count = self.counter(nums1)
        s2_count = self.counter(nums2)
        ans = []
        for i in s1_count:
            if i in s2_count:
                ans.append(i)
        return ans

    def counter(self, num):
        num_count = {}
        for i in num:
            if i not in num_count:
                num_count[i] = 1
            else:
                num_count[i] += 1
        return num_count


class Solution2(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s1_set = set(nums1)
        s2_set = set(nums2)

        return s1_set & s2_set
