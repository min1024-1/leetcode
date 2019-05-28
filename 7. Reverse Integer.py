class Solution:
    def reverse(self, x: int) -> int:
        if x>0:
            r= int(str(x)[::-1])
            if r<2**31-1:
                return r
            else:
                return 0
        elif x<0:
            r= int("-"+str(x)[::-1][:-1])
            if r>-2**31:
                return r
            else:
                return 0
        else:
            return 0
