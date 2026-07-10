import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums1 = [-x for x in nums]
        heapq.heapify(nums1)
        for i in range(k-1):
            heapq.heappop(nums1)
        return -nums1[0]