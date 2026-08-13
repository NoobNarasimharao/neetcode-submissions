class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        mp={}
        for i in s:
            if i not in mp:
                mp[i]=0
            mp[i]+=1
        mp2={}
        for i in t:
            if i not in mp:
                return False
            if i not in mp2:
                mp2[i]=0
            mp2[i]+=1
        return mp == mp2
        # return True