class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()
        while n not in seen:
            if n == 1:
                return True
            seen.add(n)
            n = self.sumOfSquares(n)    
        return False
        
    def sumOfSquares(self, n: int):
        result = 0
        while n:
            digit = n % 10
            result += digit ** 2
            n = n // 10
        return result