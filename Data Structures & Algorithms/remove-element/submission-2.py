class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp = []
        for elem in nums:
            if elem != val:
                temp.append(elem)
        for i in range(len(temp)):
            nums[i] = temp[i]
        return len(temp)