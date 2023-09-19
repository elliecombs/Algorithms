'''Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.'''

'''STEPS #Inputs clarification (integers or empty array, different data type)
#Outputs (integers or empty array, different data type)
#Potential Edge Cases & examples: (no negatives, null, floating point etc)
#Example Setup: (if not provided or code out your own)
#Pseudo Code:
#time & space Complexity; O(n)2, n total number of characters/ average length of string'''

#Portion of a string, starts at beginning = prefix 
#Time & space complexity: O(n+mn) iterate through strings once, n is total number of characters given or average size of the string.

#Solution 1
class solution:
    def longestCommonPrefix(self, strs:List[str]) -> str:
        #If no common prefix return blank/empty string
        res = ""
        
        #String is in bound
        #Simultaneously iterate through each of the indexes in the strings (pointer, i for what index we are at)
        #n
        for i in range(len(strs[0])):
        
            #Go through each string and make sure they have the same exact character
            #m 
            for s in strs:
                
                #Every string has same character at index of i, if they are equal continue if not return
                #First part if out of bounds return
                # Second conditional if in bound
                if i ==len(s)  or s[i] != strs[0]:
                    return res
            #If string is out of bounds
            
            #Addition all characters to result that is common among all strings (position i is equla to zero, append to the list)
                res += strs[0][i]
                
            #If we do have a common prefix return true
            return res 
