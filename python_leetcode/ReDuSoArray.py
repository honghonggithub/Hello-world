##Remove Duplicates from Sorted Array
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ii =0
        if nums ==[]:
        	return 0
        else:
        	i = 0
        	while i <len(nums)-1:
        		j = i+1
        		if nums[j]!=nums[i]:
        			i = j
        		else:
        			del nums[j]
        			i=i
        			# ii = ii+1

        return len(nums)
array = [1,1,2]
s = Solution()
print(s.removeDuplicates(array))    