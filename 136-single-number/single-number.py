class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = set()
        result = nums[:]
        for i in nums:
            if i not in temp:
                temp.add(i)
            else:
                result.remove(i)
                result.remove(i)
        return result[0]
                 
        