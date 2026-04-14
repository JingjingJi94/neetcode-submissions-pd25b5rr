class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res = num ^ res # XOR is commutative (a ^ b == b ^ a)and associative (a ^ b) ^ c == a ^ (b ^ c)
        return res
        