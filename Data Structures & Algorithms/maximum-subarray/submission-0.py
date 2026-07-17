class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float("-inf")
        currentSum = 0
        for n in nums:
            currentSum = max(currentSum,0)
            currentSum += n
            maxSum = max(currentSum, maxSum)
        return maxSum