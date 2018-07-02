##Valid Parentheses
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp = ['None']
        if len(s)==0:
        	return True
        elif len(s)%2!=0:
        	return False
        else:
        	for st in s:
        		if st == '(' or st =='[' or st =='{':
        			temp.append(st)
        		elif st == ')':
        			dd = temp.pop()
        			if dd!='(' or dd=='None':
        				return False
        		elif st=='}':
        			dd=temp.pop()
        			if dd!='{'or dd=='None':
        				return False
        		else:
        			dd=temp.pop()
        			if dd!='['or dd=='None':
        				return False
        	if len(temp)!=1:
        		return False
        	else:
        		return True
s = Solution()
print(s.isValid(')['))