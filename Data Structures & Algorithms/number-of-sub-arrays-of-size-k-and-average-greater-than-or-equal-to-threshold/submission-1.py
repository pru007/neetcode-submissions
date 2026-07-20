class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L= 0
        count = 0
        while L<=len(arr)-k:
            R = L+k
            if sum(arr[L:R])/k >= threshold:
                count+=1
            L+=1
        return count