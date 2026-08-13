class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cnt = float('inf')
        s = ""
        for i in strs:
            if len(i) < cnt:
                cnt = len(i)
                s = i
        cnt3 = -1
        for i in range(cnt):
            for j in strs:
                if j[i] != s[i]:
                    return s[:cnt3 + 1]
            cnt3 += 1
        return s[:cnt3 + 1]