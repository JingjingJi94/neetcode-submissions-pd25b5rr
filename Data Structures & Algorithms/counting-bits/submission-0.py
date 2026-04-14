class Solution:
    def countBits(self, n: int) -> List[int]:
        # for each integer:
        # while integer is not 0: times & 1, if is 1, increment res, 
        # shift the integer to right
        # add to output list
        output = []
        for i in range(0, n + 1):
            res = 0
            while i:
                if i & 1:
                    res += 1
                i >>= 1
            output.append(res)
        return output