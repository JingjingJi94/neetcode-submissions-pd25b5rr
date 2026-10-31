class Solution:

    def encode(self, strs: List[str]) -> str:
        # the result string has format of length#str
        res = ""
        for s in strs:
            length = len(s)
            res += str(length) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        # two pointers: 
        # i tracks the beginning of each length#str
        # j looks for delimiter '#'
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            # now j is at '#'
            length = int(s[i:j])
            i = j + 1 # move i to first letter of the str
            j = i + length
            
            string = s[i:j]

            res.append(string)
            i = j
        return res

        



