class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.sumOfSquares(n)
        while slow != fast:
            fast = self.sumOfSquares(fast)
            fast = self.sumOfSquares(fast)
            slow = self.sumOfSquares(slow)
        return True if fast == 1 else False
        
    def sumOfSquares(self, n: int):
        result = 0
        while n:
            digit = n % 10
            result += digit ** 2
            n = n // 10
        return result