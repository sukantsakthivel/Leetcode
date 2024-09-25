class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        maxs = 0
        nums.sort()
        for i in range(0,len(nums)):
            if i%2==0:
                maxs+=nums[i]
        return maxs