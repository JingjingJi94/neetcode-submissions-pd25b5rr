class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # use first column excpet first cell indicate what row needs to be zero out
        # use first row indicate what cols needs to be zeroed out
        # need a separat variable to indicate whether the first row needs to be zero out
        ROWS, COLS = len(matrix), len(matrix[0])

        # variable to tell whether first row needs to be zeroed
        rowZero = False

        # find zeros and set the first row an column to 0 for indication, use rowZero where needed
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    if r == 0:
                        rowZero = True
                        # set this row in first col to 0
                    else:
                        matrix[r][0] = 0
                    # set this column of in top row to 0
                    matrix[0][c] = 0

        #  apply markers to the inner matrix), excluding first row and column
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        #handle first column
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0

