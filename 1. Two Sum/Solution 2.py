class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range(0,len(nums)):
            rem = target - nums[i]
            if rem in h:
                return [i,h[rem]]
            else:
                h[nums[i]] = i
        return [-1,-1]
       