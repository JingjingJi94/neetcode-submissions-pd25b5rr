class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # two pointer with greedy
        #build hashmap to track the last index of each char in string
        lastIndex = {}
        for index, char in enumerate(s):
            lastIndex[char] = index
        print(lastIndex)
        output = []
        size = 0
        end = 0

        for index, char in enumerate(s):
            size += 1
            end = max(end, lastIndex[char])
            #partition for a substring ends here with stop condition:
            if index == end:
                output.append(size)
                end = 0
                size = 0
            
            
        return output