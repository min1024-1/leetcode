class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            j= target-nums[i]
            if j in nums:
                k=nums.index(target-nums[i])
                if (i!=k):
                    return [i,k]   
