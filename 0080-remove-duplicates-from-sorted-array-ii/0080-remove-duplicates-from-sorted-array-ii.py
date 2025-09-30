class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        k = 0
        for num in nums:
            if k >= 2 and num != nums[k-2]:
                nums[k] = num
                k += 1
            elif k < 2:
                k += 1
        
        return k 