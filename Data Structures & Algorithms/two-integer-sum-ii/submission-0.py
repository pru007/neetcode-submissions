class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sumMap = {}
        for i,num in enumerate(numbers):
            if target-num in sumMap:
                return [sumMap[target-num]+1,i+1]
            else:
                sumMap[num] = i