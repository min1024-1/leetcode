class Solution:
    def isValid(self, s: str) -> bool:
        dic={")":"(","]":"[","}":"{"}
        l=""
        for i,j in enumerate(s):
            if j=="(" or j=="[" or j=="{":
                l +=j
                print(j)
            elif i>0 and len(l)>0 and l[-1]==dic[j]:
                l = l[:-1]
            else:
                return False
        return len(l)==0
