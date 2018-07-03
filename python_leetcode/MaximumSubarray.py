###Maximum Subarray
class Solution(object):
    def maxSubArray(self, nums):
    	if not nums:
    		return 0
    	cursum = big = nums[0]
    	for num in nums[1:]:
    		cursum = max(num,cursum+num)
    		big = max(big,cursum)
    	return big

s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))