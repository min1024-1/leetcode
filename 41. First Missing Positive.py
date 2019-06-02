class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s=1
        while s in nums:
            s +=1
        return s
