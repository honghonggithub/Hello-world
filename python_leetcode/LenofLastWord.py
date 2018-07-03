###Length of Last Word
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = s.split(' ')
        l.reverse()

        # l.reverse()
        for num in l:
            if num!='':
                return len(num)
                break
        else:
        	return 0
  
s = Solution()
print(s.lengthOfLastWord("Today is a nice day"))
