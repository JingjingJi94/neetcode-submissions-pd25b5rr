class Solution:
    def isHappy(self, n: int) -> bool:
        #for each digit, take its square and sum them.
        # if sum not in set, add to set
        #stop condition: sum equals to 1, or sum is seen in set
        seen = set()
        while True:
            digit_sum = 0
            while n:
                digit = n % 10
                digit_sum += digit ** 2
                n = n // 10
            if digit_sum == 1:
                return True
            elif digit_sum in seen:
                return False
            else:
                seen.add(digit_sum)
                n = digit_sum
        
