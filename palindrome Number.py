class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        y = str(x)
        rev = y[::-1]
        rev1 = int(rev)
        if (rev1 == x):
            return True
        else:
            return False