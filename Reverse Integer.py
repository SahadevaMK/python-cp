class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        sign = 1

        if (x<0):
            sign = -1
            x = x*-1

        while(x>0):
            rem = x%10
            res = res*10+rem
            x= x//10
        if not -2147483648<res<2147483648:
            return 0
        res = res*sign
        return res

        