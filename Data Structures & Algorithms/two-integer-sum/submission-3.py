class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp={}
        for index, num in enumerate(nums):
            tar = target - num
            if tar in mp:
                return [mp[tar], index]
            mp[num] = index
        return [-1,-1]