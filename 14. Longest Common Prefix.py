class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l=""
        if len(strs)==0:
            return l
        a=list(map(len,strs))
        m=strs[a.index(min(a))]

        for i in range(len(m)):
            if sum(map((lambda x:x == m[i]),[x[i] for x in strs])) == len(strs):
                l += m[i]
            else:
                break
        return l
