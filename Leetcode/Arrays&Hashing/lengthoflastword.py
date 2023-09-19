'''Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
consisting of non-space characters only.

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.'''

'''STEPS #Inputs clarification (integers or empty array, different data type)
#Outputs (integers or empty array, different data type)
#Potential Edge Cases & examples: (no negatives, null, floating point etc)
#Example Setup (if not provided or code out your own)
#Pseudo Code:
#Time & Space Complexity:'''

#Time & Space Complexity O(1) 

#Solution 1
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #initialize pointers at end of string where i is index of last character in the string, - 1 index of last character and length set to 0
        i, length = len(s) - 1, 0
        
        #Eliminate white spaces from end, while the character at index i is == to white space
        while s[i] == " ":
            #Decrement towards beginning of string
            i -= 1
            
        #Count character length, i is greater than or equal to 0 and character at index i is not a space, finish counting last word
        while i >= 0 and s[i] != " ":
            
            #Decrement pointer for each iteration
            length += 1
            
            #Decrement pointer
            i -=1
        return length 