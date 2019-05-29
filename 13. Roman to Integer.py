class Solution:
    def romanToInt(self, s: str) -> int:
        nums={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        flag=1
        su=0
        l=s[::-1]
        for i in range(len(s)):
            su += flag*nums[l[i]]
            if i<= (len(s)-2) and nums[l[i]]>nums[l[i+1]]:
                flag=-1
            else:
                flag=1
        return su
