class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        # quota = float("inf")
        
        while l<=r:
            quota = (l+r)//2
            time = sum([(i//quota)+1 if i%quota>0 else (i//quota) for i in piles])
            if time > h:
                l = quota+1
            else:
                r = quota-1
        return l