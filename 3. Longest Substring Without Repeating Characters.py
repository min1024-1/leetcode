class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=""
        m=0
        for i in s:
            if i in l:
                m=max(len(l),m)
                l=l[(l.index(i)+1):]+i
            else:
                l +=i
        return max(len(l),m)
