class Solution:
    def toLowerCase(self, str: str) -> str:
        s=""
        low=ord("A")
        high=ord("Z")
        d=low-ord("a")
        for i in str:
            if ord(i)>= low and ord(i)<=high :
                s += chr(ord(i)-d)
            else:
                s +=i
        return s
