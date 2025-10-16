class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[m:] = nums2        # replace the trailing zeros with nums2
        nums1.sort() 