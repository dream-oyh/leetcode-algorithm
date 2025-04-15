import collections
class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        ans = 0
        count = collections.Counter(u+v for u in nums1 for v in nums2)
        for w in nums3:
            for p in nums4:
                if -w-p in count:
                    ans += count[-w-p]
        return ans