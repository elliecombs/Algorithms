'''

Given a numerator and a divisor of unsigned integers, 
print out the quotient and the remainder. 

You cannot use divide, cannot use mod, and you want to optimize for speed. 

31, 5 => `quotient is 6 and the remainder is 1` / [6,1] / (6,1)

'''

#Unasigned = non negative
#Examples:
#74, 4 <=[18,2]
# 13, 6 => [2, 1]
#13 is num(input 1), 6 divisor(input2), q is remainder

# Time: O(num/div)
# Space: O(?)

def solution(num, div): 
    #Intitialize at 0
    q,r = 0, 0
    
    #Important breakdown
    while (num - (div * q) >= div):
        q = q+1
        r = num - (div * q)
    print("quotient: ", q, "remainder: ", r)

solution(13, 6)

#Be sure to go as close as possible to the number for faster run time
#Goes through and checks is 0 close to 13, is 2 etc, 
#We need to reverse engineer and pseudo code before writing code & pick actual algos!!!
