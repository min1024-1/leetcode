class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in nums:
            n=nums.count(i)
            if n>=2:
                while n>1:
                    nums.pop(nums.index(i))
                    n -=1
