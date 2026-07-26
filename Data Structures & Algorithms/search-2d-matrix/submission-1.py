class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix),len(matrix[0])
        top, bottom = 0,rows-1
        while top<=bottom:
            row = (top+bottom)//2
            if target>matrix[row][-1]:
                top+=1
            elif target <matrix[row][0]:
                bottom-=1
            else:
                break
        row = (top+bottom)//2
        l,r = 0,cols-1
        while l<=r:
            col = (l+r)//2
            if target>matrix[row][col]:
                l+=1
            elif target<matrix[row][col]:
                r-=1
            else:
                return True
        return False