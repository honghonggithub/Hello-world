####Implement strStr()
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle=='':
        	return 0
        elif len(haystack)<len(needle):
        	return -1
        else:
        	return haystack.find(needle)
s = Solution()
print(s.strStr('afds', 'fs'))
