class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp={}
        for i in range(len(nums)):
            tar = target - nums[i]
            if tar in mp:
                return [mp[tar], i]
            mp[nums[i]] = i
        return [-1, -1]