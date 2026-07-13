class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights)<2:
            return 0
        leftM = [0]*len(heights)
        rightM = [0]*len(heights)
        water = [0]*len(heights)

        leftM[0] = heights[0]
        for i in range(1,len(heights)):
            leftM[i] = max(leftM[i-1],heights[i])
        rightM[-1] = heights[-1]
        for i in range(len(heights)-2,-1,-1):
            rightM[i] = max(rightM[i+1],heights[i])
        l,r = 0,len(heights)-1
        maxW = 0
        while l<r:
            width = r-l
            height = min(leftM[l],rightM[r])
            maxW = max(maxW,width*height)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return maxW