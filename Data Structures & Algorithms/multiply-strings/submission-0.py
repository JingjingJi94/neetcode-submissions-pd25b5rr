class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if '0' in [num1, num2]:
            return '0'
        # maximum number of digit for result is sum fo # digit for each str
        # this is array of INTEGERS
        res = [0] * (len(num1) + len(num2))

        #reverse both arrays so for loop is easier to think
        num1, num2 = num1[::-1], num2[::-1]

        #go backwards:
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                res[i1 + i2] += digit # !! now digit could be a two digit value, so add first, then get carry and mod
                res[i1 + i2 + 1] += res[i1 + i2] // 10
                res[i1 + i2] = res[i1 + i2] % 10
        # reverse back result, set beginning pointer to index 0
        res, beg = res[::-1], 0

        #increment passed leading zero in result (ex. 0100 -> 100)
        while beg < len(res) and res[beg] == 0:
            beg += 1
        
        # convert res array of integer to an array of strings
        res = map(str, res[beg:])
        return ''.join(res)