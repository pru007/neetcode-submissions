class Solution:
    def trap(self, height: List[int]) -> int:
        # if len(height)<2:
        #     return 0
        leftM = [0]*len(height)
        rightM = [0]*len(height)
        water = [0]*len(height)

        leftM[0] = height[0]
        for i in range(1,len(height)):
            leftM[i] = max(leftM[i-1],height[i])
        rightM[-1] = height[-1]
        for i in range(len(height)-2,-1,-1):
            rightM[i] = max(rightM[i+1],height[i])
        for i in range(len(water)):
            water[i] = min(rightM[i],leftM[i])-height[i]
        return sum(water)
        # l,r = 0,len(heights)-1
        # maxW = 0
        # while l<r:
        #     width = r-l
        #     height = min(leftM[l],rightM[r])
        #     maxW = max(maxW,width*height)
        #     if heights[l]<heights[r]:
        #         l+=1
        #     else:
        #         r-=1
        # return maxW