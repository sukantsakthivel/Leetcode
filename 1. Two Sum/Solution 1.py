class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = []
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    s.insert(0,i)
                    s.insert(1,j)
                    return s
        return [-1,-1]