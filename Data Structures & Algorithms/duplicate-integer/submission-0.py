class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictMap = {}
        for num in nums:
            if num not in dictMap:
                dictMap[num] = 1
            else:
                return True
        return False