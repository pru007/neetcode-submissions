class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumMap = {}
        for i, num in enumerate(nums):
            if num not in sumMap:
                sumMap[num] = i
        for i, num in enumerate(nums):
            if target-num in sumMap and i!=sumMap[target-num]:
                return sorted([i,sumMap[target-num]])