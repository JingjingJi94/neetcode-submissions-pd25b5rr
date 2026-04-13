class Solution:
    def checkValidString(self, s: str) -> bool:
        # buld two stack, left one for '(', one for '*'.
        # if a char is ')', first if any '(' in left stack, pop it
        # if no '(', pop from star stack
        # if there both stack are empty, and you still have unmatched ), return False

        # now there may be unmatched ( and/or *
        # if there are both kinds, compare the index of poped ( and *, 
        # if * is after (, continue, return False if not

        # return not stack. only ok to have extra  '*' left at the end, unused

        #two stacks, one for '(', one for '*'
        left = []
        star = []

        #try exhaust ')' first
        for i, char in enumerate(s):
            if char == '(':
                left.append(i)
            elif char == '*':
                star.append(i)
            else:
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False
        
        while left and star:
            if star.pop() > left.pop():
                continue
            else:
                return False
        return not left

