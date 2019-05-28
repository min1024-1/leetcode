class Solution:
    def myAtoi(self, str: str) -> int:
        flag=1
        f_s=0
        f_n=0
        r=0
        l=""
        M=2**31-1
        m=-2**31
        for i in str:
            if (i>="a" and i<="z") or (i>="A" and i<="Z") or i==".":
                break
            elif i==" ":
                if f_n or f_s:
                    break
            elif i =="+":
                if f_s or f_n :
                    break
                else:
                    f_s=1
            elif i=="-":
                if f_s or f_n:
                    break
                else:
                    flag=-1
                    f_s=1
            elif i>="0" and i <="9":
                f_n=1
                l+=i
        if l:
            r=flag*int(l)
            if r>M:
                r=M
            elif r<m:
                r=m
        return r
