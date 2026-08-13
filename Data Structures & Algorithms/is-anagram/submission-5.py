class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        mp=defaultdict(int)
        for i in s:
            mp[i]+=1
        for i in t:
            mp[i]-=1
        flg=True
        for i in mp.values():
            if i!=0:
                return False
        return True