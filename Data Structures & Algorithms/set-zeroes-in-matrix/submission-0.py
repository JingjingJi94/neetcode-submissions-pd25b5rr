class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])

        #create sets for row and col containing zero
        row = set()
        col = set()
        for r in range(n):
            for c in range(m):
                if matrix[r][c] == 0:
                    row.add(r)
                    col.add(c)
        
        # go through matrix again, turn cell with r,c in the sets to zero
        for r in range(n):
            for c in range(m):
                if r in row or c in col:
                    matrix[r][c] = 0
        
        