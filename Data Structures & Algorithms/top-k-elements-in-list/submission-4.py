class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        mp={}
        for i in nums:
            if i not in mp:
                mp[i]=1
            else:
                mp[i]+=1
        arr = sorted(mp.items(), key=lambda x: x[1], reverse=True)

        for i in range(k):
            res.append(arr[i][0])
        return res