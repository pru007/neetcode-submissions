class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        length = float("-inf")
        visit = {}
        max_freq = 0
        for i, R in enumerate(s):
            if R in visit:
                visit[R]+=1
            else:
                visit[R]=1
            max_freq = max(max_freq,visit[R])
            while (i-L+1)-max_freq>k:
                visit[s[L]]-=1
                L+=1
            length = max(length, i-L+1)
        return length

