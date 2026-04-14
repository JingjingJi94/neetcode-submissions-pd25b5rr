class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin = 0 # count of ( when treating all * as )
        leftMax = 0 # count of ( when treating all * as (

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMax < 0: #even wehn every * treated as (, we have more ) than (
                return False
            if leftMin < 0: # inpossible count below zero, clamp it to 0
                leftMin = 0
        # leftMin is the most aggressive / safest "closing" scenario (every * used as )). 
        # If even that can't get us to 0, nothing can. And if it does reach 0, we know a valid balancing exists.
        return leftMin == 0