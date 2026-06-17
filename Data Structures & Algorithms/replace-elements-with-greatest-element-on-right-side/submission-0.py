class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        out = []
        for i in range(0,len(arr)-1):
            out.append(max(arr[i+1:]))
        out.append(-1)
        return out