class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp={}
        for i in nums:
            if i not in mp:
                mp[i]=0
            mp[i]+=1
            if mp[i]>len(nums)//2:
                return i
        # tar=len(nums)//2
        # for i,j in mp.items():
        #     if j>tar:
        #         return i