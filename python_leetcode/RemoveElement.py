# ##Remove Element
# class Solution(object):
#     def removeElement(self, nums, val):
#         """
#         :type nums: List[int]
#         :type val: int
#         :rtype: int
#         """
#         i = 0
#         while i <len(nums):
#         	if nums[i]==val:
#         		del nums[i]
#         		i = i
#         		continue
#         	else:
#         		i = i+1
#         return len(nums)
# s = Solution()
# print(s.removeElement([0,1,2,2,3,0,4,2], 2))
