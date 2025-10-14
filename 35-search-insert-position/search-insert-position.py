class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target not in nums:
            nums.append(target)
        unique_nums= sorted(list(set(nums)))
         
        for i in unique_nums:
            if i==target:
                return unique_nums.index(i)
        