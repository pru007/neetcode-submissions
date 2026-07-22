class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        length = float("-inf")
        visit = {}
        for R, char in enumerate(s):
            if char in visit and visit[char] >= L:
                L = visit[char]+1
            visit[char] = R
            length = max(length,R-L+1)
        return 0 if length==float("-inf") else length