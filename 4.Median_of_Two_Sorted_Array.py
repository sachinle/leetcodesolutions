class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        index=0
        n=len(nums1)
        if n%2==0:
            mid1 = nums1[n // 2 - 1]
            mid2 = nums1[n // 2]
            median = (mid1 + mid2) / 2
        else:
            median = nums1[(n + 1) // 2 - 1]
        
        return median
