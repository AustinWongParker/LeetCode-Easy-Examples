# I didnt get this solution - grabbed from website
# Things to learn here: sets are a thing 
# Q: What is a set?
# A: In python, sets are an unordered collection of unique elements. The major difference for sets is they cannot have multiple occurences of the same element and store unordered values. 

class Solution:
    def numJewelsInStones(self, J, S):
            setJ = set(J)
            return sum(s in setJ for s in S)

        
        
'''  
#FAILED ATTEMPTS
JewelsInStones = {}
i = 0

for J in S:
    if J in JewelsInStones:
        JewelsInStones[i] += 1
    else:
        JewelsInStones[i] = 1

sum(JewelsInStones.values())
return JewelsInStones


return S.count(J)


output = 0
while J[output] == S[output]:
    output+=1
return output



for Jewels, Stones in zip(J, S):
    if J == S:
        output+=1
    else:
        break
return output
'''