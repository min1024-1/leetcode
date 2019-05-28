class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num=(nums1+nums2)
        num.sort()
        l=len(num)
        if l&1:
            return num[int((l-1)/2)]
        else:
            return (num[int(l/2)]+num[int(l/2-1)])/2
