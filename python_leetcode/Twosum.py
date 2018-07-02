##
class Solution(object):
    def twoSum(self, nums, target):
        if len(nums)<=1:
        	return False
        for i in range(len(nums)):
        	for j in range(i+1,len(nums)):
        		if nums[i]+nums[j]==target:
        			return [i,j]

nums = [2,7,11,13,9]
target=9
self = Solution()
print(self.twoSum(nums,target))