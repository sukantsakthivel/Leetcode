class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(0,len(nums2)):
            nums1.insert(m+i,nums2[i])
            if 0 in nums1:
                nums1.remove(0)
        nums1.sort()
       
 