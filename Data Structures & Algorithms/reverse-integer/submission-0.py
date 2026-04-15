# class Solution:
#     def reverse(self, x: int) -> int:
#         MIN = -2**31 # one bit is used for sign
#         MAX = 2**31 -1
#         res = 0 
#         while x:
#             digit = x % 10
#             x = x //10
#             # in JAVA, check overflow before update res, otherwise res could be wrong due to overflow
#             if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
#                 return 0
#             if res 
#             res = res * 10 + digit
#         # if res < -(2**31) or res > 2**31 - 1:
#         #     return 0
#         return res

class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648  # -2^31,
        MAX = 2147483647  #  2^31 - 1

        res = 0
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0
            if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
                return 0
            res = (res * 10) + digit

        return res