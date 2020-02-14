class Solution:
    def numberOfSteps (self, num: int) -> int:
        output = 0
        while num != 0:
            if ((num % 2) == 1): # This num will be odd
                num-=1
                output+=1
            else:
                num/=2
                output+=1
        return output
                
                