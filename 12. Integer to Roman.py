class Solution:
    def intToRoman(self, num: int) -> str:
        l=[]
        s=""
        nums={1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
        mul=1
        for j in (str(num)[::-1]):
            i=int(j)
            if i<4:
                l += nums[mul]*i
            elif i==4:
                l += nums[mul*5]+nums[mul]
            elif i==5:
                l += nums[mul*5]
            elif i<9:
                l += nums[mul]*(i-5)+nums[mul*5]
            elif i==9:
                l += nums[mul*10]+nums[mul]
            mul *=10
        return s.join(l[::-1])
