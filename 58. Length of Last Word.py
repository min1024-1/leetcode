class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        for ss in filter(None, s.split(" ")[::-1]):
            return len(ss)
        return 0
