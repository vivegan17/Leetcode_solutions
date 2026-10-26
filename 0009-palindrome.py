class Solution(object):
    def isPalindrome(self, x):
      revnum = 0
      inputn = x
      while x > 0:
        revnum = revnum*10 + x%10
        x = x//10
      if revnum == inputn:
        return True
      else :
        return False
soln.isPalindrome(x)
        