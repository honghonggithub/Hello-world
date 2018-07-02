# Palindrome Number
class Solution:
    def isPalindrome(self, x):
    	x1 = str(x)
    	xt = [i for i in x1]
    	xt.reverse()
    	xt2 = ''.join(xt)
    	if xt2==x1:
    		return True
    	else:
    		return False
self = Solution()
print(self.isPalindrome(121))
