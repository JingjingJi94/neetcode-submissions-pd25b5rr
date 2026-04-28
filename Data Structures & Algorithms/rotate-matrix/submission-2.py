class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # edit matrix in place, return nothing

        #set left and right boundary
        l, r = 0, len(matrix) - 1

        # while loop handles rotation for each layer
        while l < r:
            # rotate each cell in the same layer
            for i in range(r-l):
                #set top and bottom pointer (sqaure metrix)
                top = l
                bottom = r

                # save top left value to temp variable
                topLeft = matrix[top][l + i]

                # put bottom left to top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # put bottom right to bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # put top right to bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # put top left to top right
                matrix[top + i][r] = topLeft
            
            #update left and right
            l += 1
            r -= 1
        
