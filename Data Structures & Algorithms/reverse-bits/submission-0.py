class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1# must shift n and not 1 to get 0/1
            #find the correct spot in revered bits, and add it to res
            res += (bit << (31 - i))
        return res