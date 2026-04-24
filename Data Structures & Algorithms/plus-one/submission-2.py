class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # go backwards, edit in place.
        # if a digit < 9, just increment that digit, then terminate and return the digit list
        # else: digit resets to 0,
        n = len(digits)
        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # when digit == 9:
            digits[i] = 0
        
        return [1] + digits

        