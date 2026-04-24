class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        res = [0] * n
        carry = 1
    
        for i in range(n-1, -1, -1):
            sum = digits[i] + carry
            digit = sum % 10
            carry = sum // 10
            res[i] = digit
        if carry > 0:
            res.insert(0, carry)
        
        return res