###Search Insert Position
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums == []:
        	return 0
        elif target>nums[len(nums)-1]:
        	return len(nums)
        elif target<nums[0]:
        	return 0
        else:
        	for i in range(len(nums)):
        		if nums[i]==target:
        			return i
        			break
        	for i in range(len(nums)-1):
        		if nums[i]<target and nums[i+1]>target:
        			return i+1
        			break
# if __name__ == '__main__':
# 	print('dddddd')


s = Solution()
print(s.searchInsert([1,2,3,4,5], 6))